# Michael mangiante
# 4/3/2017
# Figure 2 - Basic statistics seperated by HUC2
# A: Cumulative First Species Observation by Plants
# B: Cumulative Annual Records by Plants
# C: Cumulative First Species Observations by Animals
# D: Cumulative Annual Records by Animals



library("reshape2")
library("ggplot2")


#load the data
setwd("H:/InvasiveSpecies/HUC2Analysis")
inData <- read.csv(file="AnimalsandPlants_HUC2Analysis_Combined_NumbFirstOccurRmvd.csv", header = TRUE, sep = ",")
names(inData)

# Color pallet
kelly_colors <- c('#8DB600', '#654522', '#F3C300', '#875692', '#F38400', '#A1CAF1', '#BE0032', '#C2B280', '#848482', '#008856', '#E68FAC', '#0067A5', '#F99379', '#604E97', '#222222', '#B3446C', '#DCD300', '#882D17')

# Select columns from dataframe
indf <- inData[,c("HUC2_Value", "Year", "Cumulative_Occurances_P", "Cumulative_First_Occurance_P", "Cumulative_Occurances_A", "Cumulative_First_Occurance_A")]

# melted data

meltdf <- melt(indf, id = c("HUC2_Value", "Year"))

head(meltdf)
levels(meltdf$variable) <- c("Cumulative Annual Plant Records", "Cumulative First Plant Species Observations", "Cumulative Annual Animal Records", "Cumulative First Animal Species Observations")


# Plot

jpeg("Figure2_bottom.jpeg", width=8.5,heigh=11, units="in", res = 600)


ggplot(meltdf, aes(Year, value, group = HUC2_Value, color=HUC2_Value))+
xlim(1900,2017)+
geom_line(aes(colour=HUC2_Value, group = HUC2_Value), size = 1) + 
#facet_grid(. ~variable, scales = "free_y") +
facet_wrap(~ variable, ncol=2, scales = "free_y")+ 
scale_colour_manual(values=kelly_colors) +
labs(color="2-Digit HUC IDs") +
guides(col = guide_legend(ncol = 2)) +
theme(legend.position = "bottom") # "right"

dev.off()

