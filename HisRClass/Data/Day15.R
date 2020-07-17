library(dplyr)
exam <- read.csv("csv_exam.csv")
exam

exam %>% filter(class==1)
exam %>% filter(english==98)
exam %>% filter(class==2)
exam %>% filter(class!=1)