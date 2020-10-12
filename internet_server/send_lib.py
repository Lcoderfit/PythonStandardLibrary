import smtplib
import email.utils
from email.mime.text import MIMEText
import tarfile
import os
import zipfile
from email.mime.multipart import MIMEMultipart


class GenerateZip:
    @staticmethod
    def make_dirs_to_zip(source_dir, zip_name):
        """将文件打包成zip压缩包"""
        print("******************zip start******************")
        with zipfile.ZipFile(zip_name, "w") as z:
            # 出去要压缩的文件的路径长度(最右边不带斜杠)
            base_path_len = len(os.path.dirname(source_dir))
            for parent, dir_names, file_names in os.walk(source_dir):
                for file_name in file_names:
                    file_path = os.path.join(parent, file_name)
                    # 在zip包中的归档路径（用相对路径表示）
                    archive_name = file_path[base_path_len:].strip(os.path.sep)
                    z.write(file_path, archive_name)
        print("******************zip end******************")


class Msg:
    def __init__(self):
        pass

    @staticmethod
    def create_msg(attach_file=None):
        # Create mail information
        # 邮件主题
        subject = "daily NiceLib.zip"
        # 发送邮件内容
        content = ""
        # 发件人
        sender = "1297611505@qq.com"
        # 收件人
        receives = ["1297611505@qq.com"]

        # 构建发送与接收信息, 发送附件的方法定义为一个变量
        msg = MIMEMultipart()
        msg.attach(MIMEText(content, 'html', 'utf-8'))  # 发送附件的方法中嵌套发送正文的方法
        msg['subject'] = subject
        msg['From'] = sender
        msg['To'] = ','.join(receives)

        # 如果没有附件，直接发送不带附件的邮件
        if not attach_file:
            return msg

        with open(attach_file, "rb") as f:
            send_data = f.read()
            original_name = os.path.split(attach_file)[-1]
            attach_dic = MIMEText(send_data, "base64", "utf8")
            attach_dic["Content-Type"] = "application/octet-stream"
            attach_dic["Content-Disposition"] = 'attachment;filename="{}"'.format(original_name)
            msg.attach(attach_dic)

        return msg


class EmailServer:
    def __init__(self):
        pass

    @staticmethod
    def config_server():
        # Configure mailbox
        config = dict()
        config['send_email'] = '1297611505@qq.com'
        config['passwd'] = 'ipjhsfzlovwfhjbh'
        config['smtp_server'] = 'smtp.qq.com'
        config['target_email'] = '1297611505@qq.com'
        return config

    def send_email(self, attach_file=None):
        """使用smtp发送带有附件的邮件到指定邮箱"""
        # 创建消息类
        msg = Msg.create_msg(attach_file)
        config = self.config_server()

        server = smtplib.SMTP()
        server.connect(host=config['smtp_server'], port=25)
        server.login(user=config['send_email'], password=config['passwd'])
        server.set_debuglevel(True)

        try:
            server.sendmail(
                config['send_email'], [config['target_email']], msg.as_string()
            )
        finally:
            server.quit()


if __name__ == '__main__':
    # 将目标文件进行压缩
    base_path = r"D:\PrivateProject\Python-Tags"
    source_dir_cur = os.path.join(base_path, r"NiceLib")
    # base_path = r"E:\SocialProject"
    # source_dir_cur = os.path.join(base_path, r"Video-Tags")
    # 最好用绝对路径，且生成zip的路径不能包含在要压缩的文件夹内部，否则会一直递归压缩，生成的zip包会越来越大
    # 如果运行生成zip的程序在需要压缩的文件夹内，则如果不用绝对路径设置压缩路径在要压缩的文件夹外部，则会产生递归压缩
    zip_file_name = r"NiceLib.zip"
    zip_name_cur = os.path.join(base_path, zip_file_name)

    # 生成zip包
    generate_zip = GenerateZip()
    generate_zip.make_dirs_to_zip(source_dir_cur, zip_name_cur)

    # 发送带有目标压缩包附件的邮件
    emailServer = EmailServer()
    emailServer.send_email(zip_name_cur)
