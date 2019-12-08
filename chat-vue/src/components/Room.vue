<template>
	<div>

		<h1> Your Room</h1>
		<li v-for="room in rooms">
			<h3>{{room.creater.username}}</h3>
			{{room.date}}
		</li>
		
	</div>
</template>

<script>
	import $ from 'jquery'

	export default{
		name:"Room",
		data() {
			return{
				rooms:'',
			}
		},
		
		created() {
			$.ajaxSetup({
				headers: {"Authorization": "Token " + sessionStorage.getItem("auth_token")},
			});
			this.loadRoom()
		},
		methods: {
			loadRoom(){
				$.ajax({
					url: "http://localhost:8000/api/v1/chat/rooms/",
					type: "GET",
					success: (response)=>{
						this.rooms=response.data.data
						console.log(response)
					}
				})
			}
		}
	}
</script>

<style>

</style>
