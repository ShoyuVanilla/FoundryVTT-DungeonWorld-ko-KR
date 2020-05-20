Hooks.on('init', () => {

	if(typeof Babele !== 'undefined') {
		Babele.get().register({
			module: 'DungeonWorld-ko',
			lang: 'ko',
			dir: 'compendium'
		}); 
	}
});
