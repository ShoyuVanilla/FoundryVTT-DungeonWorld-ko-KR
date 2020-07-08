Hooks.on('init', () => {
	if(typeof Babele !== 'undefined') {
		Babele.get().register({
			module: 'translation-dungeonworld-ko-kr',
			lang: 'ko',
			dir: 'compendium'
		});
	}
});
