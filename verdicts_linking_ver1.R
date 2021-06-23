#分別帶入common/diff_1/diff_2路徑
setwd("/Users/mingyulin/Desktop/計算法律分析/判決書/diff_3")
# 查看文件夾裡所有檔案
a = list.files()   
dir = paste("./",a,sep="") 
library(dplyr)
library(stringr)
library(readr)

#pattern="第一審判決"
dif1 = c()
location<-c()
data<-readLines(dir[1],encoding="UTF-8")
# 檔案總數
n = length(dir) 
for (i in 1:n){
  x = readLines(dir[i],encoding="UTF-8")
  sol<-lapply(x,FUN=function(x) x[1])
  sol[str_detect(string=x,pattern="第一審判決")]
  hl<-sol[str_detect(string=x,pattern="第一審判決")]
  ans<-str_sub(string=hl,start=10,end=80)
  loc<-grep("第一審判決", x)
  location<-c(location,x[loc])
  dif1<-c(dif1,ans)
}
dif1
location


#pattern="第一審刑事附帶民事訴訟判決"
dif1_n = c()
location_n<-c()
# 檔案總數
n = length(dir) 
for (i in 1:n){
  x = readLines(dir[i],encoding="UTF-8")
  sol<-lapply(x,FUN=function(x) x[1])
  sol[str_detect(string=x,pattern="第一審刑事附帶民事訴訟判決")]
  hl<-sol[str_detect(string=x,pattern="第一審刑事附帶民事訴訟判決")]
  ans<-str_sub(string=hl,start=0,end=40)
  loc<-grep("第一審刑事附帶民事訴訟判決", x)
  location_n<-c(location_n,x[loc])
  dif1_n<-c(dif1_n,ans)
}
dif1_n
location_n


#pattern="第一審附帶民事訴訟判決"
dif1_n2 = c()
location_n1<-c()
# 檔案總數
n = length(dir) 
for (i in 1:n){
  x = readLines(dir[i],encoding="UTF-8")
  sol<-lapply(x,FUN=function(x) x[1])
  sol[str_detect(string=x,pattern="第一審附帶民事訴訟判決")]
  hl<-sol[str_detect(string=x,pattern="第一審附帶民事訴訟判決")]
  ans<-str_sub(string=hl,start=10,end=80)
  loc<-grep("第一審附帶民事訴訟判決", x)
  location_n<-c(location_n,x[loc])
  dif1_n2<-c(dif1_n2,ans)
}
dif1_n2
location_n1


#pattern="第一審刑事附帶民訴判決"
dif1_n3 = c()
location_n2<-c()
# 檔案總數
n = length(dir) 
for (i in 1:n){
  x = readLines(dir[i],encoding="UTF-8")
  sol<-lapply(x,FUN=function(x) x[1])
  sol[str_detect(string=x,pattern="第一審刑事附帶民訴判決")]
  hl<-sol[str_detect(string=x,pattern="第一審刑事附帶民訴判決")]
  ans<-str_sub(string=hl,start=30,end=60)
  loc<-grep("第一審刑事附帶民訴判決", x)
  location_n<-c(location_n,x[loc])
  dif1_n3<-c(dif1_n3,ans)
}
dif1_n3
location_n2
