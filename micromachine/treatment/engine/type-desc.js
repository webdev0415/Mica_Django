import React from "react";
import {DescArr, TypeArr, relationArr} from "./arr";
export default function App() {
  let count = 0
  return (
    <div className="App">
      {
        TypeArr.map(item=>{
          const filterArr = relationArr.filter(li=>li["p"].start.properties.name === item[1])
          
          return filterArr.map(litem=> {
            const filterDesc = DescArr.filter(t=>t[1] === litem["p"].end.properties.shortName)[0]
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