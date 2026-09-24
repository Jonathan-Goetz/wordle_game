library(stringr)
library(tidy)

all_words <- read.csv("word_lists/english_words.csv")

five_letter_words <- all_words %>% 
  filter(str_length(word) == 5)
