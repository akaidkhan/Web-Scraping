


library(XML)  # Load the package
url <- "https://en.wikipedia.org/wiki/List_of_countries_by_population"



poptable <- readHTMLTable(url,which=1)
head(poptable)  

str(poptable)   # Every column is a factor. That's not what we want. 


mean(poptable$Population)    # Fails because Population is a factor
poptable$Population[1:5]    # Shows the first 5 values in the Population vector
poptable$Population <- gsub(",","",poptable$Population)
mean(poptable$Population)
str(poptable$Population) 



poptable$Population <- as.numeric(poptable$Population)
mean(poptable$Population)
str(poptable$Population)

classes <- c("integer","character","FormattedNumber","character","Percent","character")
poptable <- readHTMLTable(url,which=1,colClasses=classes,stringsAsFactors=F)

str(poptable)    # Looks pretty good now.


poptable$Date <- strptime(poptable$Date,format="%B %d, %Y")
str(poptable$Date)

poptable$Date > strptime("07/04/14",format="%m/%d/%y")

