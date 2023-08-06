# vim:ff=unix ts=4 sw=4 expandtab

import gi
import gnupg  # Requires python3-gnupg
import re
import subprocess

from os.path import expanduser

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from .config import Config
from .ui_utils import UiUtils

class GpgUtils(object):
    @staticmethod
    def get_gpg_keyring():
        # TODO: Get this working
        return gnupg.GPG()

    # TODO: Make the keys be an object instead of tuple
    @staticmethod
    def get_gpg_keys(secret=False):
        gpg = GpgUtils.get_gpg_keyring()

        keys = []

        for key in gpg.list_keys(secret):
            # print(key)
            key_id = key['keyid']
            fingerprint = key['fingerprint']

            key_name = key['uids'][0]
            if len(key_name) > 60:
                key_name = key_name[:60] + '...'

            key_friendly_name = "%s |%s|" % (key_name, key_id[-Config.KEY_ID_SIZE:])

            subkeys = []
            for subkey in key['subkeys']:
                subkeys.append(subkey[0])

            keys.append((key_id,
                         key_name,
                         key_friendly_name,
                         subkeys,
                         fingerprint))

        keys.sort(key=lambda key_tuple: key_tuple[1].lower())

        return keys

    @staticmethod
    def get_key_by_id(key_id, secret = False):
        keys = GpgUtils.get_gpg_keys(secret)

        for key_tuple in keys:
            if key_id == key_tuple[0]:
                return key_tuple

        return None

    @staticmethod
    def delete_key(key_id):
        gpg = GpgUtils.get_gpg_keyring()

        public_key = GpgUtils.get_key_by_id(key_id)
        secret_key = GpgUtils.get_key_by_id(key_id, True)

        if secret_key:
            # TODO: Confirm the deletion if we have a secret key
            print("Secret key found. Deleting it")
            result = gpg.delete_keys(secret_key[4], True)
            if not str(result) == 'ok':
                print("Failed to delete secret key (%s)" % result, secret_key)
                return False

        print("Deleting public key")
        result = gpg.delete_keys(public_key[4])

        if not str(result) == 'ok':
            print("Failed to delete public key (%s)" % result, public_key)
            return False

        return True

    @staticmethod
    def import_key(filename):
        gpg = GpgUtils.get_gpg_keyring()
        key_data = None

        if len(gpg.scan_keys(filename)) < 1:
            print("Invalid file!")
            return False

        with open (filename, "rb") as keyfile:
            key_data=keyfile.read()

        return gpg.import_keys(key_data)

    @staticmethod
    def add_gpg_keys_to_combo_box(combo_box, secret=False):
        gpg_keys_list = Gtk.ListStore(str, str)
        for key in GpgUtils.get_gpg_keys(secret):
            key_id = key[0]
            key_name = key[1]
            gpg_keys_list.append([key_id, key_name])

        cell = Gtk.CellRendererText()
        combo_box.pack_start(cell, True)
        combo_box.add_attribute(cell, 'text', 1)

        combo_box.set_model(gpg_keys_list)
        combo_box.set_entry_text_column(1)

    @staticmethod
    def encrypt_files(window, filenames, key_ids, use_armor=True, callback=None):
        conversion_list = []
        for filename in filenames:
            dest_filename = "%s.gpg" % filename
            conversion_list.append((filename, dest_filename))

        print(" - Armor:", use_armor)

        gpg = GpgUtils.get_gpg_keyring()

        for filename, dest_filename in conversion_list:
            print("Encrypting %s to %s" % (filename, dest_filename))

            with open(filename, 'rb') as src_file:
                status = gpg.encrypt_file(src_file,
                                          recipients=key_ids,
                                          always_trust=True,   # XXX: No key mgmt = no point
                                          armor=use_armor,     # XXX: This doesn't seem to work :(
                                          output=dest_filename)
            print("Status: %s" % status)

            print("Encrypted %s to %s" % (filename, dest_filename))

        # Stop spinner when we return
        if callback:
            callback(window)

        UiUtils.show_dialog(window,
                            "Completed!",
                            message_type=Gtk.MessageType.INFO)

    @staticmethod
    def sign_file(window, filename, key_id, password, use_armor=True, callback=None):
        print(" - Armor:", use_armor)
        # print(" - Password:", password)

        signature_file = "%s.sig" % filename

        print("Signing %s to %s with %s" % (filename, signature_file, key_id))

        gpg = GpgUtils.get_gpg_keyring()
        status = None
        with open(filename, 'rb') as src_file:
            status = gpg.sign_file(src_file,
                                   keyid=key_id,
                                   passphrase=password,
                                   detach=True,
                                   output=signature_file)
        print("Status: %s" % status)

        print("Signed %s to %s" % (filename, signature_file))

        # Stop spinner when we return
        if callback:
            callback(window)

        success = True
        dialog_title = "Completed!"
        message_text = "Signature can be found at:\n%s" % signature_file
        message_type = Gtk.MessageType.INFO

        if not status:
            success = False
            dialog_title = "FAILED!"
            message_text = "Unable to sign %s!" % filename
            message_type = Gtk.MessageType.ERROR

        UiUtils.show_dialog(window,
                            message_text,
                            title=dialog_title,
                            message_type=message_type)

        return success

    @staticmethod
    def decrypt_file(window, filename, password, callback=None):
        # print(" - Password:", password)

        decrypted_file = filename.rstrip('.gpg')

        print("Decrypting %s to %s" % (filename, decrypted_file))

        gpg = GpgUtils.get_gpg_keyring()
        status = None
        with open(filename, 'rb') as src_file:
            status = gpg.decrypt_file(src_file,
                                      passphrase=password,
                                      output=decrypted_file)
        print("Status: %s" % status)

        print("Decrypted %s to %s" % (filename, decrypted_file))

        # Stop spinner when we return
        if callback:
            callback(window)

        success = True
        dialog_title = "Completed!"
        message_text = "Decrypted file can be found at:\n%s" % decrypted_file
        message_type = Gtk.MessageType.INFO

        if not status:
            success = False
            dialog_title = "FAILED!"
            message_text = "Unable to decrypt %s!" % filename
            message_type = Gtk.MessageType.ERROR

        UiUtils.show_dialog(window,
                            message_text,
                            title=dialog_title,
                            message_type=message_type)

        return success

    # XXX: There's no good way though python3-gnupg to find out what
    #      type of encryption is on a file
    @staticmethod
    def get_encryped_file_info(window, filename):
        class Info(object):
            def __init__(self):
                self.is_symetric = False
                self.key_ids = []
                self.matching_key = None

        info = Info()

        # Sanity check
        try:
            subprocess.check_output(['gpg', '--version'])
        except:
            print("ERRROR! GPG not found!")
            UiUtils.show_dialog(window,
                                "ERROR! GPG binary not found in path!",
                                title="GPG not found")

            window.destroy()
            return None

        command = ['gpg', '--keyring=/dev/null', '--no-default-keyring',
                   '--list-only', '--verbose', filename]

        try:
            gpg_file_info_results = subprocess.check_output(command,
                                                            stderr=subprocess.STDOUT,
                                                            universal_newlines=True)
        except:
            print("Invalid file!")
            UiUtils.show_dialog(window,
                                "ERROR! Not a GPG-encrypted file!",
                                title="Invalid file")
            return None


        # print("Output:")
        # print(gpg_file_info_results)

        gpg_file_info_results = gpg_file_info_results.split('\n')

        key_id_regx = re.compile(' ([0-9a-fA-f]{8,16})$')
        symetric_regex = re.compile(' \d+ pass')

        for gpg_line in gpg_file_info_results:
            if not gpg_line.startswith('gpg:'):
                continue

            # print("Line:", gpg_line)

            # Extract key ids (if any)
            key_match = key_id_regx.search(gpg_line)
            if key_match:
                key_id = key_match.group(1)
                # print("Key match:", key_id)
                if key_id not in info.key_ids:
                    info.key_ids.append(key_id)

            sym_match = symetric_regex.search(gpg_line)
            if sym_match:
                # print("Symetric match")
                info.is_symetric = True

        return info

    @staticmethod
    def verify_file(window, source_filename, signature_filename=None):
        gpg = GpgUtils.get_gpg_keyring()
        print("Verifying file:", source_filename)

        verification = None

        # XXX: python-gnupg API for this is lame
        if signature_filename:
            with open(signature_filename, 'rb') as sig_file:
                print(" - Verifying with signature: ", signature_filename)
                verification = gpg.verify_file(sig_file, source_filename)
        else:
            with open(source_filename, 'rb') as src_file:
                verification = gpg.verify_file(src_file)

        print(" - Verification data:", verification)
        print(" - Fingerprint:", verification.fingerprint)
        print(" - Key ID:", verification.key_id)

        trust_level = None
        username = None
        if verification.valid:
            print("Trust level:", verification.trust_text)
            trust_level = verification.trust_level

            print("Username level:", verification.username)
            username = verification.username

        success_message = ["File %s verified!" % source_filename,
                           "User: %s" % username,
                           "Trust = %s" % verification.trust_text]

        dialog_title = "Verified!"
        message_text = '\n'.join(success_message)
        message_type = Gtk.MessageType.INFO

        if not verification.valid:
            dialog_title = "BAD SIGNATURE!"
            message_text = "Signature for %s was verified and it was bad!" % source_filename
            message_type = Gtk.MessageType.ERROR
        elif not verification.trust_level:
            dialog_title = "NOT VERIFIED!"
            message_text = "Signature for %s CANNOT be verified!\nIt was either not included or was bad!" % source_filename
            message_type = Gtk.MessageType.ERROR
        elif verification.trust_level < verification.TRUST_MARGINAL:
            dialog_title = "NOT TRUSTED ENOGUH!"
            message_text = "Signature for %s was verified but you don't trust it enough!" % source_filename
            message_type = Gtk.MessageType.ERROR

        UiUtils.show_dialog(window,
                            message_text,
                            title=dialog_title,
                            message_type=message_type)

        return verification.valid

    @staticmethod
    def check_key_password(key_id, password):
        gpg = GpgUtils.get_gpg_keyring()
        signed_data = gpg.sign("check string",
                               keyid=key_id,
                               passphrase=password)

        if str(signed_data):
            print("Password is valid!")
            return True

        # print("Password is NOT valid!")
        return False
