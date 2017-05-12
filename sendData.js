var runit=aim_url=>{
  var sender = (x,y,color)=>fetch(
    "http://canvas.ourscgy.ustc.edu.cn/canvas/modify",
    {
       headers:
       {
         "Accept": "application/json",
         "Content-Type": "application/json"
       },
       method: "POST",
       body: JSON.stringify({canvas:[{x,y,color}],count:50000}),
       mode: "cors"
    }
  )

  var crt = {}
  var exp = []
  var dif = []

  Promise.all([
    fetch(
      "http://2.718281828.xyz/canvas/update?count=-1"
    ).then(
      (res)=>res.text()
    ).then(
      text=>{
        console.log(text.length)
        console.log(text)
        json = JSON.parse(text);
        for(i of json.data){
          crt[i.x+","+i.y]=i.color
        }
      }
    ),
    fetch(
      aim_url
    ).then(
      (res)=>res.text()
    ).then(
      text=>{
        for(i of text.split("\n")){
          var p = i.split("\t")
          if(p.length!=3){
            continue
          }
          exp.push(p)
        }
      }
    )
  ]).then(
    ()=>{
      for(j of exp){
        i = [parseInt(j[0]),parseInt(j[1]),parseInt(j[2])]
        if(crt[i[0]+","+i[1]]!=i[2]){
          dif.push(i)
        }
      }
      console.log( "Num: "+(exp.length-dif.length)+" "+exp.length+"Rank: "+100.*(exp.length-dif.length)/exp.length+"%" )
    }
  ).then(
    ()=>{
      l = dif.length
      for(var i=0;i<10;i++){
        var idx = parseInt(Math.random()*l)
        sender(
          parseInt(dif[idx][0]),
          parseInt(dif[idx][1]),
          parseInt(dif[idx][2])
        )
      }
    }
  )
}

var url = 'https://raw.githubusercontent.com/hzhangxyz/canvas/master/data'

runit(url)
