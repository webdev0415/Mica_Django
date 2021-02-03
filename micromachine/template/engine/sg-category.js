import "./styles.css";
import {SGArr, SCArr, RelationArr} from "./arr"
export default function App() {
  let count = 0
  return (
    <div className="App">
      {
        SGArr.map(item=>{
          const filterArr = RelationArr.filter(li=>li["p"].start.properties.name === item[1])
          
          return filterArr.map(litem=> {
            const filterDesc = SCArr.filter(t=>t[2] === litem["p"].end.properties.code)[0]
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