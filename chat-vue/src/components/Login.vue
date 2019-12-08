<template>
	<div>
		<input v-model="login" type="text" placeholder="Логин" />
		<input v-model="password" type="password" placeholder="Пароль" />
		<button @click='setLogin'>Войти</button><br>
		{{login}} - {{password}}
	</div>
</template>

<script >
	import $ from 'jquery'

	export default {
		name: "Login",
		data() {
			return {
				login: 'zolk',
				password: '12345',
			}
		},
		methods:{
			setLogin(){
				$.ajax({
					url:"http://localhost:8000/auth/token/login/",
					type: "POST",
					data:{
						username: this.login,
						password: this.password
					},
					success:(response)=>{
						console.log(response)
						sessionStorage.setItem("auth_token", response.data.attributes.auth_token)
						this.$router.push({name:"home"})
					},
					error:(response)=>{
						if(response.status==400){
							console.log("Login or password uncorect")
						}
						console.log(response)
					}
				})
			},
		}
	}
</script>
<style scoped>
	
</style>