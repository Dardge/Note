from flask import Flask, request, render_template
import datetime,os
app = Flask(__name__)

def generate_filename(filename):
    """
    通过原始文件名称生成一个由时间戳来组成的新文件名
    :param filename: 原始文件名称
    :return: 生成的新文件名
    """
    ftime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
    ext = filename.split('.')[-1]
    filename = ftime + '.' + ext
    return filename

def generate_upload_path(file,dirname,filename):
    """
    生成上传的文件路径
    :param file: 获取当前文件的跟路径的文件
    :param dirname: 保存文件的具体目录
    :param filename: 保存的文件名称
    :return:
    """
    base_dir = os.path.dirname(file)
    upload_path = os.path.join(base_dir,dirname,filename)
    return upload_path

@app.route('/01-file',methods=['GET','POST'])
def file_views():
    if request.method == 'GET':
        return render_template('01-file.html')
    else:
        #1.接受前端传递过来的图片
        if 'uimg' in request.files:
            file = request.files['uimg']
            #2.拼年月日十分秒微秒作为文件名称
            ftime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            #3.获取上传文件的扩展名
            ext = file.filename.split('.')[-1]
            filename = ftime + '.' + ext
            #4.准备上传路径
            basedir = os.path.dirname(__file__)
            print("basedir:" , basedir)

            #5.拼上传的完整路径
            # basedir+"/static/"+filenamer
            upload_path = os.path.join(basedir,"static",filename)
            file.save(upload_path)
            return "上传文件成功!"

@app.route('/02-file-exer',methods=['GET','POST'])
def file_exer():
    if request.method == 'GET':
        return render_template('02-file-exer.html')
    else:
        title = request.form['title']
        type = request.form['type']
        content = request.form['content']

        print("标题:%s,类型:%s,内容:%s" % (title,type,content))

        #判断文件上传
        if 'img' in request.files:
            file = request.files['img']
            filename = generate_filename(file.filename)
            up_path = generate_upload_path(__file__,"static/upload",filename)
            print("保存路径:",up_path)
            file.save(up_path)
        return "获取数据成功!"





if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5555)







