<html>
	<h1>one vec index array for USER LIST</h1>
	<{foreach from=$arr1 item=temp key=k}>
		<{$k}>=<{$temp}>
	<{/foreach}>
	<p>===================</p>
	<h1>one vec assoc array for  USER LIST</h1>
	<{foreach from=$arr2 item=temp key=k}>
		<{$k}>=<{$temp}>
	<{/foreach}>

	<p>===================</p>
	<h1>two vec index array for  USER LIST</h1>
	<{foreach from=$arr3 item=temp key=k1}>
		<{foreach from=$temp item=val key=k2}>
			<{$k2}>=<{$val}>
		<{/foreach}>
	<br/>
	<{/foreach}>

	<p>===================</p>
	<h1>two vec assoc array for  USER LIST</h1>
	<{foreach from=$arr4 item=temp key=k1}>
		<{foreach from=$temp item=val key=k2}>
			<{$k2}>=<{$val}>
		<{/foreach}>
	<br/>
	<{/foreach}>

	<p>===================</p>
	<h1>two vec assoc array for  USER LIST "if"</h1>
	<{foreach from=$arr4 item=temp key=k1}>
		<{foreach from=$temp item=val key=k2}>
			<{if $k2 ne 'age'}>
				<{$k2}>=<{$val}>
			<{/if}>
		<{/foreach}>
	<br/>
	<{/foreach}>

	<p>===================</p>
	<h1>two vec assoc array for  USER LIST "if else elseif"</h1>
	<{foreach from=$arr4 item=temp key=k1}>
		<{if $temp.age > 40 }>
			older
		<{else}>
			<h2>younger</h2>
		<{/if}>
	<br/>
	<{/foreach}>
	

</html>
