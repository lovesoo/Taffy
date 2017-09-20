# coding=utf-8

import base64
from Crypto.Hash import MD5
from Crypto.Hash import SHA
from Crypto.Hash import HMAC
from Crypto.Cipher import DES
from Crypto.Cipher import DES3
from Crypto.Cipher import AES

# Modes of padding
PAD_NORMAL = 1
PAD_PKCS5 = 2
PAD_PKCS7 = 3


class Security(object):
    """加密类，定义常用加密方法"""

    def __init__(self):
        pass

    def _padData(self, data, pad, padmode, block_size=8):
        # Pad data depending on the mode
        # block_size = 8
        if pad and padmode == PAD_PKCS5:
            raise ValueError("Cannot use a pad character with PAD_PKCS5")

        if padmode == PAD_NORMAL:
            if len(data) % block_size == 0:
                # No padding required.
                return data
            if not pad:
                raise ValueError("Data must be a multiple of " + str(block_size)
                                 + " bytes in length. Use padmode=PAD_PKCS5 or set the pad character.")
            data += (block_size - (len(data) % block_size)) * pad

        elif padmode == PAD_PKCS5 or padmode == PAD_PKCS7:
            pad_len = block_size - (len(data) % block_size)
            data += pad_len * chr(pad_len)

        return data

    def _unpadData(self, data):
        """目前只支持pkcs5,7的unpad"""
        # Pad data depending on the mode
        # block_size = 8
        padlen = ord(data[-1])
        return data[0:-padlen]

    def getDES(self, key, data, mode=DES.MODE_ECB, IV=None, pad=None, padmode=PAD_PKCS5):
        """DES加密
        :param key: 秘钥key
        :type key: string
        :param data: 未加密数据
        :type data: string
        :param mode: 加密模式
        :type mode: ECB/CBC/CFB
        :param IV: The initialization vector to use for encryption or decryption
        :type IV: string
        :param pad: Optional argument, set the pad character (PAD_NORMAL) to use during all encrypt/decrpt operations done with this instance
        :type pad: string
        :param padmode: Optional argument, set the padding mode (PAD_NORMAL or PAD_PKCS5)
        :type padmode: PAD_NORMAL/PAD_PKCS5/PAD_PKCS7
        """
        data = self._padData(data, pad, padmode, block_size=DES.block_size)
        cipher = DES.new(key, mode=mode)
        return cipher.encrypt(data)

    def decodeDES(self, key, data, mode=DES.MODE_ECB, IV=None, pad=None, padmode=PAD_PKCS5):
        """DES解密
        :param key: 秘钥key
        :type key: string
        :param data: 加密数据
        :type data: string
        :param mode: 加密模式
        :type mode: ECB/CBC/CFB
        :param IV: The initialization vector to use for encryption or decryption
        :type IV: string
        :param pad: Optional argument, set the pad character (PAD_NORMAL) to use during all encrypt/decrpt operations done with this instance
        :type pad: string
        :param padmode: Optional argument, set the padding mode (PAD_NORMAL or PAD_PKCS5)
        :type padmode: PAD_NORMAL/PAD_PKCS5/PAD_PKCS7
        """
        cipher = DES.new(key, mode=mode)
        plaintext = cipher.decrypt(data)
        plaintext = self._unpadData(plaintext)
        return plaintext

    def getDES3(self, key, data, mode=DES3.MODE_ECB, IV=None, pad=None, padmode=PAD_PKCS5):
        """DES3加密
        :param key: 秘钥key
        :type key: string
        :param data: 未加密数据
        :type data: string
        :param mode: 加密模式
        :type mode: ECB/CBC/CFB
        :param IV: The initialization vector to use for encryption or decryption
        :type IV: string
        :param pad: Optional argument, set the pad character (PAD_NORMAL) to use during all encrypt/decrpt operations done with this instance
        :type pad: string
        :param padmode: Optional argument, set the padding mode (PAD_NORMAL or PAD_PKCS5)
        :type padmode: PAD_NORMAL/PAD_PKCS5/PAD_PKCS7
        """
        data = self._padData(data, pad, padmode, block_size=DES3.block_size)
        cipher = DES3.new(key, mode=mode)

        return cipher.encrypt(data)

    def decodeDES3(self, key, data, mode=DES3.MODE_ECB, IV=None, pad=None, padmode=PAD_PKCS5):
        """DES3解密
        :param key: 秘钥key
        :type key: string
        :param data: 未加密数据
        :type data: string
        :param mode: 加密模式
        :type mode: ECB/CBC/CFB
        :param IV: The initialization vector to use for encryption or decryption
        :type IV: string
        :param pad: Optional argument, set the pad character (PAD_NORMAL) to use during all encrypt/decrpt operations done with this instance
        :type pad: string
        :param padmode: Optional argument, set the padding mode (PAD_NORMAL or PAD_PKCS5)
        :type padmode: PAD_NORMAL/PAD_PKCS5/PAD_PKCS7
        """
        cipher = DES3.new(key, mode=mode)
        plaintext = cipher.decrypt(data)
        plaintext = self._unpadData(plaintext)
        return plaintext

    def getHMAC_SHA1(self, secret, data):
        """获取HMAC-SHA1
        :param secret: 秘钥key
        :type secret: string
        :param data: 未加密数据
        :type data: string
        """

        h = HMAC.new(secret, digestmod=SHA)
        h.update(data)
        return h.hexdigest()

    def getSHA(self, data):
        """获取SHA
        :param data: 未加密数据
        :type data: string
        """
        m = SHA.new()
        m.update(data)
        return m.hexdigest()

    def getMD5(self, data):
        """获取MD5
        :param data: 未加密数据
        :type data: string
        """
        m = MD5.new()
        m.update(data)
        return m.hexdigest()

    def getAES(self, key, data, mode=AES.MODE_ECB, pad=None, padmode=PAD_PKCS5):
        """加密方法，返回密文
        :param data: 未加密数据
        :type data: string
        MODE_CBC 16位
        #这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
        """
        data = self._padData(data, pad, padmode, block_size=AES.block_size)
        cipher = AES.new(key, mode=mode)
        return cipher.encrypt(data)

    def getBase64(self, data):
        """返回base64
        :param data: 转换前数据
        :type data: string
        """
        return base64.b64encode(data)

    def decodeBase64(self, data):
        """返回base64
        :param data: 转换前数据
        :type data: string
        """
        return base64.b64decode(data)
