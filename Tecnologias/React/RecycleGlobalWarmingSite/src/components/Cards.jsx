

const Card=({imgSrc="",title="",message=""}) =>{

    return(


        <div className='cards'>
          <div>
            <img  src={imgSrc} className='cardsImage'/>
          </div>
          <div className="cardLetters">
              <h2>{title}</h2>
               <a>{message}</a>
          </div>
        </div>
    );
}
export default Card;