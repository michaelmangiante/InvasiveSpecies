# Michael Mangiante
# builds plots with lines for each HUC2
# 3/27/2017

library("reshape2")
library("ggplot2")


#load the data
setwd("H:/InvasiveSpecies/HUC2Analysis/HUCSummary")
inData <- read.csv(file="HUCSummary_Combined_AllYears_StrLabels_numbFirstOccurRemoved.csv", header = TRUE, sep = ",")

names(inData)

cbbPalette <- c("#000000", "#654522", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "#66FF33", "#00CCFF", "#00FFFF", "#00CC99", "#FF9933", "#CCCC99", "#CC0033", "#9900FF", "#CCFFFF", "#FFCC00")
kelly_colors <- c('#8DB600', '#654522', '#F3C300', '#875692', '#F38400', '#A1CAF1', '#BE0032', '#C2B280', '#848482', '#008856', '#E68FAC', '#0067A5', '#F99379', '#604E97', '#222222', '#B3446C', '#DCD300', '#882D17')
joinsData = data.frame(Year = inData$Year, HUC2 = inData$HUC2_Value, InputVariable = inData$Annual_Occurances)
meltdata <- melt(inData, id = c("HUC2_Value", "Year"))
head(meltdata)
levels(meltdata$variable) <- c("Total Annual Records", "Cumulative Annual Records", "Annual Number of Species", "Cumulative First Species Observations", "Annual HUC12s with Records", "Annual HUC12 Sq. Km.", "Annual HUC8s with Records", "Annual HUC8 Sq. Km.")

head(meltdata)
col2rgb(kelly_colors)

###

jpeg("TestPlot.jpeg", width=11,heigh=8.5, units="in", res = 600)

ggplot(meltdata, aes(Year, value, group = HUC2_Value, color=HUC2_Value))+
xlim(1900,2017)+
geom_line(aes(colour=HUC2_Value, group = HUC2_Value), size = 1) + 
#facet_grid(. ~variable, scales = "free_y") +
facet_wrap(~ variable, ncol=3, scales = "free_y")+ 
scale_colour_manual(values=kelly_colors) +
labs(color="2-Digit HUC IDs")


dev.off()

# colors: https://gist.github.com/ollieglass/f6ddd781eeae1d24e391265432297538




################################### OLD CRAP I DONT NEED

# subsets

HUC1 <- subset(joinsData, HUC2 == "1")
HUC2 <- subset(joinsData, HUC2 == "2")
HUC3 <- subset(joinsData, HUC2 == "3")
HUC4 <- subset(joinsData, HUC2 == "4")
HUC5 <- subset(joinsData, HUC2 == "5")
HUC6 <- subset(joinsData, HUC2 == "6")
HUC7 <- subset(joinsData, HUC2 == "7")
HUC8 <- subset(joinsData, HUC2 == "8")
HUC9 <- subset(joinsData, HUC2 == "9")
HUC10 <- subset(joinsData, HUC2 == "10")
HUC11 <- subset(joinsData, HUC2 == "11")
HUC12 <- subset(joinsData, HUC2 == "12")
HUC13 <- subset(joinsData, HUC2 == "13")
HUC14 <- subset(joinsData, HUC2 == "14")
HUC15 <- subset(joinsData, HUC2 == "15")
HUC16 <- subset(joinsData, HUC2 == "16")
HUC17 <- subset(joinsData, HUC2 == "17")
HUC18 <- subset(joinsData, HUC2 == "18")

annualCount <- ggplot() + 
	geom_line(data = HUC1, aes(x = Year, y = InputVariable, group = "HUC1", color = "red"))+
	geom_line(data = HUC2, aes(x = Year, y = InputVariable, group = "HUC2", color = "green))+
	geom_line(data = HUC3, aes(x = Year, y = InputVariable, color = "blue"))+
	geom_line(data = HUC4, aes(x = Year, y = InputVariable, color = "purple"))+
	geom_line(data = HUC5, aes(x = Year, y = InputVariable, color = "orange"))+
	geom_line(data = HUC6, aes(x = Year, y = InputVariable, color = "yellow"))+
	geom_line(data = HUC7, aes(x = Year, y = InputVariable, color = "black"))+
	geom_line(data = HUC8, aes(x = Year, y = InputVariable, color = "coral2"))+
	geom_line(data = HUC9, aes(x = Year, y = InputVariable, color = "yellow4"))+
	geom_line(data = HUC10, aes(x = Year, y = InputVariable, color = "violetred3"))+
	geom_line(data = HUC11, aes(x = Year, y = InputVariable, color = "linen"))+
	geom_line(data = HUC12, aes(x = Year, y = InputVariable, color = "limegreen"))+
	geom_line(data = HUC13, aes(x = Year, y = InputVariable, color = "grey51"))+
	geom_line(data = HUC14, aes(x = Year, y = InputVariable, color = "darkslateblue"))+
	geom_line(data = HUC15, aes(x = Year, y = InputVariable, color = "darkslategray2"))+
	geom_line(data = HUC16, aes(x = Year, y = InputVariable, color = "hotpink2"))+
	geom_line(data = HUC17, aes(x = Year, y = InputVariable, color = "cadetblue3"))+
	geom_line(data = HUC18, aes(x = Year, y = InputVariable, color = "chocolate2"))+
	xlab("Year") +
	xlim(c(1980, 2018)) +
	ylab("Annual Number of Plant Records")
annualCount

ggplot(meltdata, aes(x=Year, y = variable, color = HUC2_Value))+
geom_line()
facet_wrap(~name + variable)


###
ggplot(meltdata, aes(Year, value, color = HUC2_Value))+
geom_point()
geom_smooth(method = "lm", se = FALSE) +
facet_wrap(. ~variable)
