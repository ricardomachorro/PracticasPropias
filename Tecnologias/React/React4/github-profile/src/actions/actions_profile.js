export const PROFILE_FETCHED="INFO_FETCHED";
export const PROFILE_EDITED="PROFILE_EDITED";

export function fetchProfile(){
  return (dispatch)=>{

    fetch('https://api.github.com/users/ricardomachorro',{
      method:'GET',
      headers:header
    })
    .then(response=> response.json())
    .then(json=>{
      this.setState({
        userInfo:json
      })
      console.log(json);

    })
    .catch(error=>{
      console.log(error);
    });
    let header=new Headers({"Content-Type":"application/json","Authorization":"token de44f224dbc507630d2e309e9eb4a44fd8654cbb"});
    return fetch("https://api.github.com/users/ricardomachorro",{
      method:"GET",
      headers:header
    })
    .then(response=>response.json())
    .then(json=>{
      console.log(json)
      dispatch(loadProfile(json))
    })
    .catch(error=>console.log(error));
  }
}


export function saveProfile(profile){
  return (dispatch)=>{

    fetch('https://api.github.com/users/ricardomachorro',{
      method:'GET',
      headers:header
    })
    .then(response=> response.json())
    .then(json=>{
      this.setState({
        userInfo:json
      })
      console.log(json);

    })
    .catch(error=>{
      console.log(error);
    });
    let header=new Headers({"Content-Type":"application/json","Authorization":"token de44f224dbc507630d2e309e9eb4a44fd8654cbb"});
    return fetch("https://api.github.com/user",{
      method:"PATCH",
      headers:header,
      body:JSON.stringify(profile)
    })
    .then(response=>response.json())
    .then(json=>{
      console.log(json)
      dispatch(loadProfile(json))
    })
    .catch(error=>console.log(error));
  }
}

export function loadProfile(results){
  return{
    type: PROFILE_FETCHED,
    payload:results
  }
}
