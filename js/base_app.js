
// ##############################
function showTip(message){
    const tip_id = Math.random()
    let tip = `
    <div data-tip-id="${tip_id}" class="flex justify-center w-full lg:w-1/3 mx-auto py-4 text-white bg-purple-500 rounded-md">
      ${message}
    </div>
    `
    document.querySelector("#tips").insertAdjacentHTML("afterbegin", tip)
    setTimeout(function(){
        document.querySelector(`[data-tip-id='${tip_id}']`).remove()
    }, 3000)
}

// ##############################
async function login(){
    const frm = event.target
    const btn = frm.querySelector("button")
    btn.disabled = true
    btn.innerText = btn.getAttribute("data-await")
    const conn = await fetch("/api-login", {
        method : "POST",
        body : new FormData(frm)
    })
    btn.disabled = false
    btn.innerText = btn.getAttribute("data-default")
    const data = await conn.json()
    if( !conn.ok ){
        console.log("Cannot login")
        showTip(data.info)        
        return
    }	
    // Success
    location.href = `/${data.user_name}`
}

// ##############################
async function sign_up(){
	const frm = event.target
	const btn = frm.querySelector("button")
    btn.disabled = true
    btn.innerText = btn.getAttribute("data-await")
    const conn = await fetch("/api-sign-up", {
        method : "POST",
        body : new FormData(frm)
    })
    btn.disabled = false
    btn.innerText = btn.getAttribute("data-default")
	const data = await conn.json()
	console.log(data)
    if( !conn.ok ){
        console.log(data.info)
        showTip(data.info)        
        return
    }
    // Success
    location.href = `/${data.user_name}`
}

// ##############################
async function tweet(){
    const btn = event.target
    btn.disabled = true
    btn.innerText = btn.getAttribute("data-await")
    const frm = event.target.form
    const conn = await fetch("/api-tweet", {
        method : "POST",
        body : new FormData(frm)
    })
    btn.disabled = false
    btn.innerText = btn.getAttribute("data-default")
	const div_tweet = await conn.text()
    if( !conn.ok ){
        console.log("Cannot tweet")
        showTip("ups...")        
        return
    }
    // Success
	try{
		frm.reset()		
		document.querySelector("#tweets").insertAdjacentHTML("afterbegin", div_tweet)
	}catch(ex){
		console.error(ex)
	}
    console.log("ok tweet")
}


// ##############################
async function follow_unfollow(user_followee_id){
    const btn = event.target
	const api = btn.innerText == "Follow" ? "/api-follow" : "/api-unfollow"
	const dom_profile_total_following = document.querySelector("#profile_total_following")
	const dom_profile_total_followers = document.querySelector("#profile_total_followers")
    btn.disabled = true
    // btn.innerText = btn.getAttribute("data-await")
    const frm = new FormData()
	frm.append("user_followee_id", user_followee_id)
    const conn = await fetch(api, {
        method : "POST",
        body : frm
    })
    btn.disabled = false
	const data = await conn.json()
    if( !conn.ok ){
        console.log(data)
        showTip(data.info)        
        return
    }
	if(api == "/api-follow"){
		dom_profile_total_followers.innerText = parseInt(dom_profile_total_followers.innerText) + 1
	}else{
		dom_profile_total_followers.innerText = parseInt(dom_profile_total_followers.innerText) - 1 
	}
	btn.innerText = api == "/api-follow" ? "Unfollow" : "Follow"    
    // Success
    console.log("ok follow")
}


// ##############################
async function send_gold_code(){
    const btn = event.target
    btn.disabled = true	
    // btn.innerText = btn.getAttribute("data-await")
    const conn = await fetch("/api-send-gold-code", {
        method : "POST"
    })
    // btn.disabled = false
	const data = await conn.json()
	console.log(data)
    if( !conn.ok ){
		btn.disabled = false
		btn.innerText = btn.getAttribute("data-final")
        console.log(data.info)
        showTip(data.info)        
        return
    }
	btn.innerText = btn.getAttribute("data-final")	
}


// ##############################
async function verify_gold_code(){
    const btn = event.target
    btn.disabled = true
	const frm = event.target.form
    btn.innerText = btn.getAttribute("data-await")
    const conn = await fetch("/api-verify-gold-code", {
        method : "POST",
		body : new FormData(frm)
    })
	const data = await conn.json()
	console.log(data)
    if( !conn.ok ){
		btn.disabled = false
		btn.innerText = btn.getAttribute("data-default")
        console.log(data.info)
        showTip(data.info)        
        return
    }
	// Success gold verified, reload the whole page
	location.href = `/${data.user_name}`
}


// ##############################
function show_search_results(){
	document.querySelector("#search_results").classList.remove("hidden")
}
function hide_search_results(){
	document.querySelector("#search_results").classList.add("hidden")
}

let the_timer
function search(){
	clearTimeout(the_timer)
	the_timer = setTimeout( async function(){
		const conn = await fetch("/search", {
			method : "POST"
		})
		const data = await conn.json()
		console.log(data)
	}, 500 );
}




















