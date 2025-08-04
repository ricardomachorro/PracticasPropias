import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { navBarOptions } from './data/generalData'
import NavBarComponent from './components/NavBarComponent'
import MainContainer from './components/MainContainer'
import HomeComponent from './components/HomeComponent'
import FundingComponent from './components/FundingComponent'
import ActionsComponent from './components/ActionsComponent'
import ValuesComponent from './components/ValuesComponent'
import './AppOwn.css'

function App() {
  //const [count, setCount] = useState(0)

   const optionsNavBar = navBarOptions;
   const [optionSelected, setOptionSelected] = useState("Home");

  return (

    <MainContainer>
           <NavBarComponent
            optionsNav ={optionsNavBar}
            actionChange={setOptionSelected}
          />

        { optionSelected=="Home" && <HomeComponent/>}

        {optionSelected=="Funding" && <FundingComponent/>}

        {optionSelected=="Actions" && <ActionsComponent/>}

        {optionSelected=="Values" && <ValuesComponent/>}


    </MainContainer>

    
  
    
  )
}

export default App
