library(arules)
library(arulesViz)
library(readr)
dataset <- read_csv("C:/Users/arnab/Documents/Spring2017/TIM245/project/crime_prediction/association/crimesbyday2015.csv")
#path is where the file is located , e.g. “/Users/tylermunger/Documents/tim245/hw3/”
#dataset <- read.csv("$PATH#/survey_dataset.csv ")

#convert the dataset to nominal attributes so that it is suitable for rule mining
dataset <- data.frame(sapply(dataset, function(x) as.factor(as.character(x))))

#n is the number of rules we want to examine
n = 10
support <- 0.1
confidence <- 0.5

#generate the rules
rules <- apriori(dataset, parameter = list(supp=support, conf=confidence))

#a rule is redundant if a more general rules with the same or a higher confidence exists
rules.pruned = rules[!is.redundant(rules)]
#plot the pruned rules with respect to support, confidence, and lift
plot(rules.pruned)

#sort by lift and take the top n
rules.pruned.sorted <- sort(rules.pruned, by="lift")
top_n_rules <- head(rules.pruned.sorted, n=n)

#print out the top rules
inspect(top_n_rules)

#visualize the top-n rules
plot(top_n_rules, method="graph", control=list(type="items"))
