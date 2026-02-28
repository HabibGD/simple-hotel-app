import { useState } from "react"
import data from "../utils/data"

function Accordian() {

    const [ accordan, setAccordant ] = useState(data)
    const [ enableMulty, setEnableMulty ] = useState(false)

    const displayContent = (id) => {
        setAccordant(prevAccordan => prevAccordan.map(accordan => {
            if(!enableMulty){
                return accordan.id === id ? { ...accordan, isActive: !accordan.isActive } : { ...accordan, isActive: false }
            }

            return accordan.id === id ? { ...accordan, isActive: !accordan.isActive } : accordan
        }) )
    }


  return (
    <>
        <button onClick={() => setEnableMulty(prev => !prev)} className="cursor-pointer font-bold text-zinc-100 bg-amber-900 w-50 text-center mb-3 p-3">{ enableMulty ? "Desable Multiple": "Enable multiple" } </button>
        {
            accordan.map(dataObj => (
            <div className="bg-amber-900 w-100 text-center m-1 p-2" key={dataObj.id}>
                <div onClick={() =>  displayContent(dataObj.id)} className="flex flex-row justify-between cursor-pointer">
                    <span className="ml-3 text-amber-100 font-normal pb-1"> {dataObj.question}</span>
                    <span  className="font-extrabold text-amber-50">+</span>
                </div>

                { dataObj.isActive && <p className="text-amber-50"> { dataObj.answer }  </p> }
            </div>
            ))
        }
       
    </>
  )
}

export default Accordian