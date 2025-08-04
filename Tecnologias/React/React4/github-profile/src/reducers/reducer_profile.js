import {
  PROFILE_FETCHED,PROFILE_EDITED
} from "../actions/actions_profile"

const profile=(state=[],action)=>{
  switch(action.type){
    case PROFILE_FETCHED:
    return action.payload
    case PROFILE_EDITED:
       var newState=JSON.parse(JSON.stringify(state));
       newState=replaceProfile(newState,action.payload)
    return action.payload
    default:
    return state
  }
}

export default profile

function replaceProfile(profiles,newProfile){
  var newProfiles=[];
  profiles.forEach(function(thisProfile){
    if(thisProfile.name=newProfiles.name){
      newProfiles.push(newProfile);
    }else{
      newProfiles.push(thisProfile);
    }
  })
  return newProfiles;
}
