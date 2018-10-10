# coding=utf-8
import base64
from Crypto.Hash import MD5
from Crypto.Hash import SHA
from Crypto.Hash import HMAC
from Crypto.Cipher import DES
from Crypto.Cipher import DES3
from Crypto.Cipher import AES
from Crypto.Util import Padding


class Security(object):
    """加密类，定义常用加密方法"""

    def __init__(self):
        pass

    def getDES(self, key, data, mode=DES.MODE_ECB, block_size=8, style='pkcs7'):
        """
        DES加密
        :param key: 秘钥key
        :param data: 未加密数据
        :param mode: 加密模式
            :var MODE_ECB: :ref:`Electronic Code Book (ECB) <ecb_mode>`
            :var MODE_CBC: :ref:`Cipher-Block Chaining (CBC) <cbc_mode>`
            :var MODE_CFB: :ref:`Cipher FeedBack (CFB) <cfb_mode>`
            :var MODE_OFB: :ref:`Output FeedBack (OFB) <ofb_mode>`
            :var MODE_CTR: :ref:`CounTer Mode (CTR) <ctr_mode>`
            :var MODE_OPENPGP:  :ref:`OpenPGP Mode <openpgp_mode>`
            :var MODE_EAX: :ref:`EAX Mode <eax_mode>`

        :param block_size: 填充block大小：默认为8
        :param style: 填充算法：‘pkcs7’(default),‘iso7816’or‘x923’
        :return: 加密结果 byte string
        """

        data = Padding.pad(data.encode('utf-8'), block_size=block_size, style=style)
        cipher = DES.new(key.encode('utf-8'), mode=mode)

        return cipher.encrypt(data)

    def decodeDES(self, key, data, mode=DES.MODE_ECB, block_size=8, style='pkcs7'):
        """
        DES解密
        :param key: 秘钥key
        :param data: 未加密数据
        :param mode: 加密模式
            :var MODE_ECB: :ref:`Electronic Code Book (ECB) <ecb_mode>`
            :var MODE_CBC: :ref:`Cipher-Block Chaining (CBC) <cbc_mode>`
            :var MODE_CFB: :ref:`Cipher FeedBack (CFB) <cfb_mode>`
            :var MODE_OFB: :ref:`Output FeedBack (OFB) <ofb_mode>`
            :var MODE_CTR: :ref:`CounTer Mode (CTR) <ctr_mode>`
            :var MODE_OPENPGP:  :ref:`OpenPGP Mode <openpgp_mode>`
            :var MODE_EAX: :ref:`EAX Mode <eax_mode>`

        :param block_size: 填充block大小：默认为8
        :param style: 填充算法：‘pkcs7’(default),‘iso7816’or‘x923’
        :return: 解密结果 byte string
        """
        cipher = DES.new(key.encode('utf-8'), mode=mode)
        plaintext = cipher.decrypt(data)
        plaintext = Padding.unpad(plaintext, block_size=block_size, style=style)
        return plaintext

    def getDES3(self, key, data, mode=DES3.MODE_ECB, block_size=8, style='pkcs7'):
        """
        DES3加密
        :param key: 秘钥key
        :param data: 未加密数据
        :param mode: 加密模式
            :var MODE_ECB: :ref:`Electronic Code Book (ECB) <ecb_mode>`
            :var MODE_CBC: :ref:`Cipher-Block Chaining (CBC) <cbc_mode>`
            :var MODE_CFB: :ref:`Cipher FeedBack (CFB) <cfb_mode>`
            :var MODE_OFB: :ref:`Output FeedBack (OFB) <ofb_mode>`
            :var MODE_CTR: :ref:`CounTer Mode (CTR) <ctr_mode>`
            :var MODE_OPENPGP:  :ref:`OpenPGP Mode <openpgp_mode>`
            :var MODE_EAX: :ref:`EAX Mode <eax_mode>`

        :param block_size: 填充block大小：默认为8
        :param style: 填充算法：‘pkcs7’(default),‘iso7816’or‘x923’
        :return: 加密结果 byte string
        """
        data = Padding.pad(data.encode('utf-8'), block_size=block_size, style=style)
        cipher = DES3.new(key.encode('utf-8'), mode=mode)
        return cipher.encrypt(data)

    def decodeDES3(self, key, data, mode=DES3.MODE_ECB, block_size=8, style='pkcs7'):
        """
        DES3解密
        :param key: 秘钥key
        :param data: 未加密数据
        :param mode: 加密模式
            :var MODE_ECB: :ref:`Electronic Code Book (ECB) <ecb_mode>`
            :var MODE_CBC: :ref:`Cipher-Block Chaining (CBC) <cbc_mode>`
            :var MODE_CFB: :ref:`Cipher FeedBack (CFB) <cfb_mode>`
            :var MODE_OFB: :ref:`Output FeedBack (OFB) <ofb_mode>`
            :var MODE_CTR: :ref:`CounTer Mode (CTR) <ctr_mode>`
            :var MODE_OPENPGP:  :ref:`OpenPGP Mode <openpgp_mode>`
            :var MODE_EAX: :ref:`EAX Mode <eax_mode>`

        :param block_size: 填充block大小：默认为8
        :param style: 填充算法：‘pkcs7’(default),‘iso7816’or‘x923’
        :return: 解密结果 byte string
        """
        cipher = DES3.new(key, mode=mode)
        plaintext = cipher.decrypt(data)
        plaintext = Padding.unpad(plaintext, block_size=block_size, style=style)
        return plaintext

    def getHMAC_SHA1(self, secret, data):
        """获取HMAC-SHA1
        :param secret: 秘钥key
        :type secret: string
        :param data: 未加密数据
        :type data: string
        """
        h = HMAC.new(secret.encode('utf-8'), digestmod=SHA)
        h.update(data.encode('utf-8'))
        return h.hexdigest()

    def getSHA(self, data):
        """获取SHA
        :param data: 未加密数据
        :type data: string
        """
        m = SHA.new()
        m.update(data.encode('utf-8'))
        return m.hexdigest()

    def getMD5(self, data):
        """获取MD5
        :param data: 未加密数据
        :type data: string
        """
        m = MD5.new()
        m.update(data.encode('utf-8'))
        return m.hexdigest()

    def getAES(self, key, data, mode=AES.MODE_ECB, block_size=8, style='pkcs7'):
        """AES加密
        :param key: 秘钥key
        :param data: 未加密数据
        :param mode: 加密模式
            :var MODE_ECB: :ref:`Electronic Code Book (ECB) <ecb_mode>`
            :var MODE_CBC: :ref:`Cipher-Block Chaining (CBC) <cbc_mode>`
            :var MODE_CFB: :ref:`Cipher FeedBack (CFB) <cfb_mode>`
            :var MODE_OFB: :ref:`Output FeedBack (OFB) <ofb_mode>`
            :var MODE_CTR: :ref:`CounTer Mode (CTR) <ctr_mode>`
            :var MODE_OPENPGP:  :ref:`OpenPGP Mode <openpgp_mode>`
            :var MODE_EAX: :ref:`EAX Mode <eax_mode>`

        #这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用

        :param block_size: 填充block大小：默认为8
        :param style: 填充算法：‘pkcs7’(default),‘iso7816’or‘x923’
        :return: 加密结果 byte string
        """

        data = Padding.pad(data.encode('utf-8'), block_size=block_size, style=style)
        cipher = AES.new(key.encode('utf-8'), mode=mode)
        return cipher.encrypt(data)

    def getBase64(self, data):
        """返回base64
        :param data: 转换前数据
        :type data: string
        """
        return base64.b64encode(data.encode('utf-8'))

    def decodeBase64(self, data):
        """返回base64
        :param data: 转换前数据
        :type data: string
        """
        return base64.b64decode(data)
