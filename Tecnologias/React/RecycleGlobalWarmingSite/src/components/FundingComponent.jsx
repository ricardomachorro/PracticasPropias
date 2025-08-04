import ExpositionMessage from "./ExpositionMessage";
import fundActions from "../data/fundingData";


const FundingComponent=({})=>{
    return(
        <div className="fundingContainer">
            {
                fundActions.map((fundAction)=>{
                    return(
                        <ExpositionMessage
                          title={fundAction.title}
                          message={fundAction.message}
                          imgSrc={fundAction.img}

                        />
                    );
                })
            }
        </div>
    );
}

export default FundingComponent;