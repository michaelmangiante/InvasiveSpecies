# Michael Mangiante
# Figure 1
# 1a: Total Number of Annual Species
# 1b: Cumulative Number of First Occurance Species
# 1c: Total Number of Annual Records
# 1d: Total Number of HUC12 with Species

library("reshape2")
library("ggplot2")

setwd("K:/InvasiveSpecies/FinalData/Figures_plants_animals")
inData <- read.csv(file="Combined_PlantAnimal_data.csv", header = TRUE, sep=",")

names(inData)
head(inData)

selectData <- inData[,c("Type", "Year", "SpeciesCount", "CumulativeFirstOccuranceCount","TotalNumbOccurance", "HUC12Count")]
meltdata <- melt(selectData, id=c("Year", "Type"))
levels(meltdata$variable) <- c("Total Number of Species Observed Annually", "Cumulative Number of First Occurance Records", "Total Number of Annual Records", "Annual Number of HUC12s with Records")
lineType <- c("dashed", "solid")
head(meltdata)

###
jpeg("Figure1.jpeg", width=11,heigh=11, units="in", res = 600)


ggplot(meltdata, aes(Year, value, group = Type, color = Type))+
xlim(1850, 2017) +
geom_line(aes(colour = Type, group = Type, linetype = Type), size = 1)+
facet_wrap(~variable, ncol=2, scales = "free_y") +
theme_bw()+
theme(panel.border = element_blank(), panel.grid.major = element_blank(), panel.grid.minor = element_blank(), axis.line= element_line(colour = "black"),
text = element_text(size=15))

dev.off()