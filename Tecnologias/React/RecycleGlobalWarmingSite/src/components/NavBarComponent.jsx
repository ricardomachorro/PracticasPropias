import LogoEarth from "../assets/LogoEarth.png"


const NavBarComponent =({optionsNav=[],actionChange})=>{
    return(
        <div className="navBar">
            <div >
                <img className="logoNavBar" src={LogoEarth}/>
            </div>

            <div className="navBarOptions">
                {optionsNav.map((option)=>{
                    return(
                    <a onClick={()=>{actionChange(option)}}>{option}</a>
                    );
                })}
            </div>
          
           
        </div>
    );
}

export default NavBarComponent;