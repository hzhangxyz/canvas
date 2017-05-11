data = ImageData[ImageResize[src, {80, 80}]];
ans = Flatten[
   Table[sample = data[[i, j]]; {i, j, 
     Floor[((sample[[1]]*256 + sample[[2]])*256 + 
         sample[[3]])*256]}, {i, 1, 80}, {j, 1, 80}], 1];
Export["C:\\Users\\zh199\\Desktop\\test\\canvas\\data", ans, "Table"]
