define({
    getCode: function(faction){
        switch(faction){
            case 'Cygnar':
                return 'CY';
                break;
            case 'The Protectorate of Menoth':
                return 'ME';
                break;
            case 'Khador':
                return 'KD';
                break;
            case 'Cryx':
                return 'CX';
                break;
            case 'Retribution of Scyrah':
                return 'RT';
                break;
            case 'Convergence of Cyriss':
                return 'CV';
                break;
            case 'Mercenaries':
                return 'MC';
                break;
            case 'Trollbloods':
                return 'TR';
                break;
            case 'Circle Orboros':
                return 'CO';
                break;
            case 'Skorne':
                return 'SK';
                break;
            case 'Legion of Everblight':
                return 'LG';
                break;
            case 'Minions':
                return 'MN';
                break;
        }
    },
    getFaction: function(code){
        switch(code){
            case 'CY':
                return 'Cygnar';
                break;
            case 'ME':
                return 'The Protectorate of Menoth';
                break;
            case 'KD':
                return 'Khador';
                break;
            case 'CX':
                return 'Cryx';
                break;
            case 'RT':
                return 'Retribution of Scyrah';
                break;
            case 'CV':
                return 'Convergence of Cyriss';
                break;
            case 'MC':
                return 'Mercenaries';
                break;
            case 'TR':
                return 'Trollbloods';
                break;
            case 'CO':
                return 'Circle Orboros';
                break;
            case 'SK':
                return 'Skorne';
                break;
            case 'LG':
                return 'Legion of Everblight';
                break;
            case 'MN':
                return 'Minions';
                break;
        }
    }
});
