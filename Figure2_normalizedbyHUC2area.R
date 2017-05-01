# Michael mangiante
# 4/13/2017
# Figure 2 - Basic statistics seperated by HUC2
# A: Cumulative First Species Observation by Plants normalized by HUC2 area
# B: Cumulative Annual Records by Plants normalized by HUC2 area
# C: Cumulative First Species Observations by Animals normalized by HUC2 area
# D: Cumulative Annual Records by Animals normalized by HUC2 area



library("reshape2")
library("ggplot2")


#load the data
setwd("H:/InvasiveSpecies/HUC2Analysis")
inData <- read.csv(file="AnimalsandPlants_HUC2Analysis_Combined_NumbFirstOccurRmvd.csv", header = TRUE, sep = ",")
names(inData)

# Color pallet
kelly_colors <- c('#8DB600', '#654522', '#F3C300', '#875692', '#F38400', '#A1CAF1', '#BE0032', '#C2B280', '#848482', '#008856', '#E68FAC', '#0067A5', '#F99379', '#604E97', '#222222', '#B3446C', '#DCD300', '#882D17')

# Select columns from dataframe
indf <- inData[,c("HUC2_Value", "Year", "Cumulative_Occurances_P_HUC2normalized", "Cumulative_First_Occurance_P_HUC2normalized", "CumulativeHUC12Area_ProportionofTotal_P", "Cumulative_Occurances_A_HUC2normalized", "Cumulative_First_Occurance_A_HUC2normalized", "CumulativeHUC12Area_ProportionofTotal_A")]

# melted data

meltdf <- melt(indf, id = c("HUC2_Value", "Year"))

head(meltdf)
levels(meltdf$variable) <- c("Cumulative Annual Plant Records", "Cumulative First Plant \nSpecies Observations", "Proportional Accumulation of HUC12 \nSq. Km. with Plant Observations", "Cumulative Annual Animal Records", "Cumulative First Animal \nSpecies Observations", "Proportional Accumulation of HUC12 \nSq. Km. with Animal Observations")


# Plot

jpeg("Figure2_normalized.jpeg", width=11,heigh=8.5, units="in", res = 600)


ggplot(meltdf, aes(Year, value, group = HUC2_Value, color=HUC2_Value))+
xlim(1900,2017)+
geom_line(aes(colour=HUC2_Value, group = HUC2_Value), size = 1) + 
#facet_grid(. ~variable, scales = "free_y") +
facet_wrap(~ variable, ncol=3, scales = "free_y")+ 
scale_colour_manual(values=kelly_colors) +
labs(color="2-Digit HUC IDs") +
guides(col = guide_legend(ncol = 2)) +
theme_bw()+
theme(legend.position = "bottom", panel.border = element_blank(), panel.grid.major = element_blank(), panel.grid.minor = element_blank(), axis.line= element_line(colour = "black")) 
# "right" or "bottom

dev.off()

