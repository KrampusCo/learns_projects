<template>
	<div>
		<h1> Chat use VueJS</h1>
		<button v-if='!auth' @click='goLogin'>Вход</button>
		<button v-else  @click='logout'>Выход</button>
		<Room v-if="auth"></Room>
	</div>
</template>

<script>
	import Room from "@/components/Room.vue"

	export default {
		name: 'Home',
		components:{
			Room
		},
		computed:{
			auth(){
				if(sessionStorage.getItem("auth_token")){
					return true
				}
			}
		},
		methods: {
			goLogin(){
				this.$router.push({name:"Login"})
			},
			logout(){
				sessionStorage.removeItem("auth_token")
				window.location='/'
			}
		}
	}
</script>

<style>

</style>
