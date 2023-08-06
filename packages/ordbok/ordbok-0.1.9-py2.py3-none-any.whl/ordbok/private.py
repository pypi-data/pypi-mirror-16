import os
import sys
import yaml
import simplecrypt
from ordbok import ConfigFile, open_wrapper


def decrypt_content(key, content):
    content = simplecrypt.decrypt(key, content)
    if sys.version_info[0] < 3:
        return content
    else:
        return str(content.decode('utf8'))


def encrypt_content(key, content):
    return simplecrypt.encrypt(key, content)


class PrivateConfigFile(ConfigFile):
    def _load_yaml(self):
        content = self._load_and_decrypt_file()
        return yaml.load(content)

    def _load_encrypted_file(self):
        try:
            with open_wrapper(self.config_file_path + u'.private', 'rb') as f:
                return f.read()
        except IOError:
            if os.path.exists(self.config_file_path):
                raise Exception(
                    "Encrypted version of private config file '{0}' "
                    "not found. Please run `ordbok encrypt {0}`."
                    "".format(self.config_file_path))
            else:
                raise Exception(
                    "Private config file '{0}' not found. "
                    "Please create and run `ordbok encrypt {0}`."
                    "".format(self.config_file_path))

    def _load_decrypted_file(self):
        try:
            with open_wrapper(self.config_file_path, 'r+') as f:
                return f.read()
        except IOError:
            raise Exception("{} not found.".format(self.config_file_path))

    def _save_encrypted_file(self):
        content = self._load_decrypted_file()
        content = self._encrypt_content(content)
        with open_wrapper(self.config_file_path+'.private', 'wb') as f:
            f.write(content)

    def _save_decrypted_file(self):
        content = self._load_and_decrypt_file()
        with open_wrapper(self.config_file_path, 'w') as f:
            f.write(content)

    def _load_and_decrypt_file(self):
        content = self._load_encrypted_file()
        return self._decrypt_content(content)

    def _decrypt_content(self, content):
        return decrypt_content(self.config.private_file_key, content)

    def _encrypt_content(self, content):
        return encrypt_content(self.config.private_file_key, content)
