import "./styles.css";
import * as DescArr from "../treatmenttypedesc.json"
import * as relationCPT from "../desc-cpt.json"
import * as relationSnomed from "../desc-snomed.json"

export default function App() {
  let count = 0;
  return (
    <div className="App">
      {
      DescArr.map((item, idx)=>{
        count = count + 1
        const detectSnomed = relationSnomed.filter(li=>li["p"].start.properties.shortName === item["n"].properties.shortName)[0]
        const detectCPT = relationCPT.filter(li=>li["p"].start.properties.shortName === item["n"].properties.shortName)[0]
        return (
          <span key={idx}>{`('${count}', 
          '${item["n"].properties.shortName}', 
          '${item["n"].properties.longName}',
          ${item["n"].properties.defaultValue},
          ${item["n"].properties.priority},
          ${item["n"].properties.typeDescID},
          '${item["n"].properties.description}',
          '{${detectSnomed["p"].end.properties.conceptID}}',
          '{${detectCPT["p"].end.properties.cptCode}}',
          ),
          `}<br /></span>
        )
      })
    }
    </div>
  );
}
