# Michael Mangiante
# 4.13.2017
# Bar Chart for collectors of invasive animal and plant species

library("reshape2")
library("ggplot2")

setwd("K:/InvasiveSpecies/FinalData/Figures_plants_animals")
inData <- read.csv(file="Collector_data.csv", header = TRUE, sep=",")

selectdata <- inData[,c("ID", "Type", "TotalObservations")]

names(inData)
head(inData)

meltdata <- melt(inData, id=c("ID", "Type"))

levels(meltdata$variable) <-c("Total Number of Observations", "Number of First Occurance Observations")
#levels(meltdata$ID) <-c("Federal Agency", "State/Local/Tribe", "University (or associated Museum)", "Independent Museum", "NGO/Partnership", "Other")
meltdata$ID2 <- factor(meltdata$ID, as.character(meltdata$ID))
head(meltdata)


###
jpeg("Collector_barplot_blankLabel.jpeg", width=11,heigh=8.5, units="in", res = 600)


ggplot(data=meltdata, aes(ID, value)) +
geom_bar(aes(x=ID2, fill= Type), position = "dodge", stat = "identity") +
facet_wrap(~variable, ncol=2, scales = "free_y") +
labs(x = "")+
#scale_x_discrete(labels=c("Federal Agency", "State/Local/Tribe", "University /n(or associated Museum)", "Independent Museum", "NGO/Partnership", "Other"))+
theme_bw()+
theme(panel.border =element_rect(colour = "black", fill=NA), panel.grid.major = element_blank(), panel.grid.minor = element_blank(), axis.line= element_line(colour = "black"),
axis.text.x=element_text(angle=45,hjust=1, vjust=1), text = element_text(size = 15), strip.text = element_blank())

dev.off()

