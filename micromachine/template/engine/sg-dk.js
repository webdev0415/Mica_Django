import "./styles.css";
import {SGDKArr, DKSArr} from "./arr"
export default function App() {
  let count = 0
  return (
    <div className="App">
      {
        SGDKArr.map(item=>{

          return item[1].map(li=>{
            count = count + 1
            const filterArr = DKSArr.filter(cl=>cl[1] === li)[0]
            return (
              <span>
                {`(${count},
                ${item[0]},
                ${filterArr[0]}),`}
              <br /></span>
            )
          })
        })
        
      }
    </div>
  );
}