
import Card from './Cards'
import { cardsHome } from '../data/homeData';

const HomeComponent =({})=>{

    return(
    <div className="homeContainer">

      {cardsHome.map((card)=>{
        return(
          <Card 
          imgSrc={card.img}
          title={card.title}
          message={card.message} />
        );
      })}
      
      
    </div>);
}

export default HomeComponent;