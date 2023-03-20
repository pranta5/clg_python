library(rvest)

url <- "https://www.technoindiauniversity.ac.in/"
response <- read_html(url)
data <- response %>% html_nodes(".single-content")

result <- list()
for (i in data){
  s_name <- html_node(i, "a") %>% html_text()
  details <- html_node(i, "p") %>% html_text()
  result <- c(result, list(c(s_name, details)))
}
print(result)
