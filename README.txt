Git 全局设置
git config --global user.name "tddey"
git config --global user.email "liujicun01@gmail.com"

创建新版本库
git clone https://git.99safe.org/tddey/source-py.git
cd source-py
touch README.md
git add README.md
git commit -m "add README"
git push -u origin master

已存在的文件夹
cd existing_folder
git init
git remote add origin https://git.99safe.org/tddey/source-py.git
git add .
git commit -m "Initial commit"
git push -u origin master

已存在的 Git 版本库
cd existing_repo
git remote rename origin old-origin
git remote add origin https://git.99safe.org/tddey/source-py.git
git push -u origin --all
git push -u origin --tags
