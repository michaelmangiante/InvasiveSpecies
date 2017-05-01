# Michael Mangiante
# Figure 1
# 1a: Total Number of Annual Species
# 1b: Cumulative Number of First Occurance Species
# 1c: Total Number of Annual Records
# 1d: Total Number of HUC12 with Species

library("reshape2")
library("ggplot2")
library("plyr")
library("dplyr")
library("grid")


setwd("K:/InvasiveSpecies/FinalData/Figures_plants_animals")
inData <- read.csv(file="Combined_PlantAnimal_data.csv", header = TRUE, sep=",")

names(inData)
head(inData)

selectData <- inData[,c("Type", "Year", "SpeciesCount", "CumulativeFirstOccuranceCount","CumulativeOccurance", "CumulativeHUC12WithRecrods")]
meltdata <- melt(selectData, id=c("Year", "Type"))
levels(meltdata$variable) <- c("Total Number of Species Observed Annually", "Cumulative Number of First Occurance Records", "Cumulative Number of Annual Records", "Cumulative Number of HUC12s with Records")
lineType <- c("dashed", "solid")
head(meltdata)

grob = grobTree(textGrob("(a)", x = 0.1, y = 0.95, hjust = 0, gp = gpar(col="black", fontsize = 13)))
grob2 = grobTree(textGrob("(b)", x = 0.1, y = 0.95, hjust = 0, gp = gpar(col="black", fontsize = 13)))
myLabels <- data.frame(cyl = c(4,6,8, 12), label = c("(a)", "(b)", "(c)", "(d)"))

###
jpeg("Figure1_blanklabels.jpeg", width=11,heigh=11, units="in", res = 600)


ggplot(meltdata, aes(Year, value, group = Type, color = Type))+
xlim(1850, 2017) +
geom_line(aes(colour=Type, group = Type), linetype = "dashed", size = 1) + 
geom_line(aes(colour = Type, group = Type), linetype = "solid", subset(meltdata, Year <=2005), size = 1)+
facet_wrap(~variable, ncol=2, scales = "free_y") +
theme_bw()+
theme(panel.border =element_rect(colour = "black", fill=NA), panel.grid.major = element_blank(), panel.grid.minor = element_blank(), axis.line= element_line(colour = "black"),
text = element_text(size=15), strip.text = element_blank()) 
#geom_text(x = 1870, y = 100, aes(label=label), data=myLabels)

#geom_text(data = data.frame(x=1870,y=100, label = c("(a)", "(b)", "(c)", "(d)"), color = c("1", "2", "3", "4")), aes(x,y, label = label), inherit.aes=FALSE)

#label = c("(a)", "(b)", "(c)", "(d)")
#annotation_custom(grob)

#annotate("text", label = "(a)", x = 1870, y = 100)

dev.off()
