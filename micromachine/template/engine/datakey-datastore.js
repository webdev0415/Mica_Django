import React from "react"
import {DKSArr, DSArr, RelationArr} from "./arr"
export default function App() {
  let count = 0
  return (
    <div className="App">
      {
        DKSArr.map(item=>{
          const filterArr = RelationArr.filter(li=>li["p"].start.properties.code === item[4])
          
          return filterArr.map(litem=> {
            const filterDesc = DSArr.filter(t=>t[2] === litem["p"].end.properties.code)[0]
            count = count + 1
            return (
              <span>
                {`(${count},
                ${item[0]},
                ${filterDesc[0]}
              ),`}
              <br /></span>
            )
          })
        })
      }
    </div>
  );
}
