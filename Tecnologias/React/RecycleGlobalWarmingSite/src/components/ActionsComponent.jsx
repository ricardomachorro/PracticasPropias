import actions from '../data/actionsData'
import Card  from './Cards';


const ActionsComponent =({})=>{


    return(
        <div className='actionsContainer'>
            {actions.map((action)=>{
                return(
                    <Card
                      title={action.title}
                      message={action.message}
                      imgSrc={action.img}
                    />
                );
            })}
        </div>
    );
}

export default ActionsComponent;