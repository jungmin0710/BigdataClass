library(readxl)
df_exam <- read_excel("excel_exam.xlsx")
df_exam

mean(df_exam$english)

mean(df_exam$science)


df_exam_novar <- read_excel("excel_exam_novar.xlsx",col_names = F)
df_exam_novar


df_exam_sheet <- read_excel("excel_exam_sheet.xlsx",sheet = 3)
df_exam_sheet
           

df_csv_exam <- read.csv("csv_exam.csv")
df_csv_exam

df_csv_exam <- read.csv("csv_exam.csv", stringsAsFactors = F)
df_csv_exam

df_midterm <- data.frame(english = c(90,80,60,70), math = c(50,60,100,20), class = c(1,1,2,2))
df_midterm

write.csv(df_midterm, file = "df_midterm.csv")


install.packages("ggplot2")
library(ggplot2)
mpg <- as.data.frame(ggplot2::mpg)
mpg

head(mpg)
head(mpg,10)
tail(mpg)
tail(mpg,10)
View(mpg)
dim(mpg)
str(mpg)
summary(mpg)

install.packages("dplyr")
library(dplyr)

df_raw <- data.frame(var1 = c(1,2,1), var2 = c(2,3,2))
df_raw

df_new <- df_raw
df_new

df_new <- rename(df_new, v2 = var2)
df_new

df_raw
df_new

library(ggplot2)
copy_mpg <- mpg
copy_mpg <- rename(copy_mpg, city = cty)
copy_mpg <- rename(copy_mpg, highway = hwy)
head(copy_mpg)

df <- data.frame(var1 = c(4,3,8), var2 = c(2,6,1))
df
df$var_sum <- df$var1 + df$var2
df
df$var_mean <- (df$var1 + df$var2) /2
df

copy_mpg$total <- (copy_mpg$city + copy_mpg$highway)/2
head(copy_mpg)
mean(copy_mpg$total)

summary(copy_mpg$total)
hist(copy_mpg$total)


copy_mpg$test <- ifelse(copy_mpg$total>=20,"pass","fail")

copy_mpg
head(copy_mpg)
table(copy_mpg$test) #table은 빈도표
qplot(copy_mpg$test)

copy_mpg$grade <- ifelse(copy_mpg$total >= 30, "A",
                    ifelse(copy_mpg$total >=20, "B", "c"))

head(copy_mpg,5)
qplot(copy_mpg$grade)

copy_mpg$grade2 <- ifelse(copy_mpg$total >= 30, "A",
                        ifelse(copy_mpg$total >= 25, "B",
                            ifelse(copy_mpg$total >=20, "C", "D")))

copy_mpg


