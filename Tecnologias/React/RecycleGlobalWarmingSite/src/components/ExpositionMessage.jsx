

const ExpositionMessage =({title="",message="",imgSrc=""}) =>{

    return(
        <div className="expositionMessage">
            <div>
                 <img src={imgSrc}  className="expositionMessageImage"/>
            </div>
            <div className="expositionMessageLetters">
                <h2>{title}</h2>
                <a>{message}</a>
            </div>

        </div>
    );


}

export default ExpositionMessage;