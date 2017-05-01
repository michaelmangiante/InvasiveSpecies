# Circular Figure for Plants from Source Region
# 4/10/2017
# https://github.com/gjabel/migest/blob/master/demo/cfplot_reg2.R
# for HUC2 first occurances

library("circlize")
library("reshape2")

# load data
setwd("K:/InvasiveSpecies/FinalData/plantsDB/CircularFlow")
#inData <- read.csv(file="Plants_USFirstOccurance_CircularFlowData.csv", header=TRUE, sep=",")
#metadata <- read.csv(file="Circle_metadata3.csv", header = TRUE, sep=",")

inData <- read.csv(file="Plants_HUC2FirstOccurance_CircularFlowData.csv", stringsAsFactors = FALSE)
metadata <- read.csv(file="Circle_metadata_HUC2FirstOccurance.csv", stringsAsFactors=FALSE)

names(inData)
head(inData)

# melt the data
#selectData <- inData[,c("US_Regions", "Neotropics", "Western.Palearctic", "North.Africa", "Central.and.South.Africa", "Eastern.Palearctic", "Southeast.Asia", "Australia.New.Zealand")]
meltdata <- melt(inData, id="Regions")
# remove possible NAs
meltdata[is.na(meltdata)]=0

head(meltdata)
head(metadata)

kelly_colors <- c('#8DB600', '#654522', '#F3C300', '#875692', '#F38400', '#A1CAF1', '#BE0032', '#C2B280', '#848482', '#008856', '#E68FAC', '#0067A5', '#F99379', '#604E97')


#print jpeg
jpeg("Plants_CircularPlot_FirstHUC2Occurance.jpeg", width=11,heigh=11, units="in", res = 600)



## Plot Parameters

chordDiagram(x = meltdata)
circos.clear()
circos.par(start.degree = 90, gap.degree = 4, track.margin = c(-0.1, 0.1), points.overflow.warning = FALSE)
par(mar = rep(0, 4))

##
##chord diagram with user selected adjustments for bilateral migration flow data
##

chordDiagram(x = meltdata, grid.col = metadata$col1, transparency = 0.25,
             order = metadata$region, directional = 1,
             direction.type = c("arrows", "diffHeight"), diffHeight  = -0.04,
             annotationTrack = "grid", annotationTrackHeight = c(0.05, 0.1),
             link.arr.type = "big.arrow", link.sort = TRUE, link.largest.ontop = TRUE)

## Add in Labels and axis


circos.trackPlotRegion(
  track.index = 1, 
  bg.border = NA, 
  panel.fun = function(x, y) {
    xlim = get.cell.meta.data("xlim")
    sector.index = get.cell.meta.data("sector.index")
    reg1 = metadata$reg1[metadata$region == sector.index]
	reg2 = metadata$reg2[metadata$region == sector.index]
    
    circos.text(x = mean(xlim), y = ifelse(test = nchar(reg2) == 0, yes = 5.2, no = 6.0), 
                labels = reg1, facing = "bending", cex = 1.2)
    circos.text(x = mean(xlim), y = 4.4, 
                labels = reg2, facing = "bending", cex = 1.2)
    circos.axis(h = "top", 
                major.at = seq(from = 0, to = xlim[2], by = ifelse(test = xlim[2]>10, yes = 20, no = 4)), 
                minor.ticks = 1, major.tick.percentage = .5,
                labels.niceFacing = FALSE)
  }
)

dev.off()