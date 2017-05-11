data = ImageData[ImageResize[src, {80, 80}]];
ans = Flatten[
   Table[sample = data[[i, j]]; {j + 120, i, 
     Floor[(Floor[sample[[1]]*255]*256 + Floor[sample[[2]]*255])*256 +
        Floor[sample[[3]]*255]]}, {i, 1, 80}, {j, 1, 80}], 1];
Export["C:\\Users\\zh199\\Desktop\\test\\canvas\\data", ans, "Table"]
