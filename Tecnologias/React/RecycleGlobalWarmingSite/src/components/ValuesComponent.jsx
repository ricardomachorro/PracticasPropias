import values from '../data/valuesData'
import ExpositionMessage from './ExpositionMessage';

const ValuesComponent =({})=>{

    return(
        <div className="valuesContainer">
            {values.map((value)=>{
                return(
                   <ExpositionMessage
                      title={value.title}
                      message={value.message}
                      imgSrc={value.img}
                   />
                );
            })}
        </div>
    );
}

export default ValuesComponent;