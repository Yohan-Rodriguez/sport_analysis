

def list_delete_links():
    
    list_del_link = [
                        'https://www.sofascore.com/tournament/basketball/el-salvador/lmb/17343',
                        'https://www.sofascore.com/tournament/basketball/czech-republic/cesky-pohar/19678',
                        'https://www.sofascore.com/tournament/basketball/croatia-amateur/medunarodni-turnir-sjecanja-na-kresimira-cosica/20451',
                        'https://www.sofascore.com/tournament/basketball/international/americas-league/1242',
                        'https://www.sofascore.com/tournament/basketball/international/central-american-and-caribbean-games/11305',
                        'https://www.sofascore.com/tournament/basketball/international/united-league-super-cup/17283',
                        'https://www.sofascore.com/tournament/basketball/france/match-des-champions-women/10588',
                        'https://www.sofascore.com/tournament/basketball/international/u18-fiba-eurobasket-div-a-women/898',
                        'https://www.sofascore.com/tournament/basketball/international/asian-games-men/10707',
                        'https://www.sofascore.com/tournament/basketball/brazil/nbb-all-star/20067',
                        'https://www.sofascore.com/tournament/basketball/turkey/all-star-game/14626',
                        'https://www.sofascore.com/tournament/basketball/international/aswbl/1534',
                        'https://www.sofascore.com/tournament/basketball/philippines/pba-commissioner-cup/1656',
                        'https://www.sofascore.com/tournament/basketball/international/fiba-world-cup-qualification-americas/10461',
                        'https://www.sofascore.com/tournament/basketball/international/u20-fiba-eurobasket-div-b-women/891',
                        'https://www.sofascore.com/tournament/basketball/croatia-amateur/business-basketball-league/18326',
                        'https://www.sofascore.com/tournament/basketball/croatia-amateur/old-stars-zagreb/20475',
                        'https://www.sofascore.com/tournament/basketball/international/fiba-americup-qualification/14711',
                        'https://www.sofascore.com/tournament/basketball/international/liga-aba-super-cup/11468',
                        'https://www.sofascore.com/tournament/basketball/international/liga-sudamericana/1936',
                        'https://www.sofascore.com/tournament/basketball/international/u18-fiba-eurobasket-div-a/895',
                        'https://www.sofascore.com/tournament/basketball/spain/super-cup-acb/581',
                        'https://www.sofascore.com/tournament/basketball/philippines/pba-philippine-cup/1956',
                        'https://www.sofascore.com/tournament/basketball/international/fiba-eurobasket-women/659',
                        'https://www.sofascore.com/tournament/basketball/australia/nbl1-east/18403',
                        'https://www.sofascore.com/tournament/basketball/international/int-friendly-games/871',
                        'https://www.sofascore.com/tournament/basketball/serbia/2-muska-liga/17298',
                        'https://www.sofascore.com/tournament/basketball/australia/nbl1-women/13488',
                        'https://www.sofascore.com/tournament/basketball/international/u18-fiba-americas/11119',
                        'https://www.sofascore.com/tournament/basketball/croatia-amateur/treca-muska-liga-centar/19956',
                        'https://www.sofascore.com/tournament/basketball/usa/national-invitation-tournament/18640',
                        'https://www.sofascore.com/tournament/basketball/international/olympic-games/276',
                        'https://www.sofascore.com/tournament/basketball/greece-amateur/te-eok-dodekanese/19838',
                        'https://www.sofascore.com/tournament/basketball/international/liga-unike/16827',
                        'https://www.sofascore.com/tournament/basketball/international/olympic-games-women/440',
                        'https://www.sofascore.com/tournament/basketball/poland/2-liga/19660',
                        'https://www.sofascore.com/tournament/basketball/international/u18-fiba-eurobasket-div-b-women/899',
                        'https://www.sofascore.com/tournament/basketball/turkey/federation-cup/19322',
                        'https://www.sofascore.com/tournament/basketball/international/u18-european-challengers-women/17049',
                        'https://www.sofascore.com/tournament/basketball/international/fiba-womens-world-cup/442',
                        'https://www.sofascore.com/tournament/basketball/italy/coppa-italia-a1-femminile/10196',
                        'https://www.sofascore.com/tournament/basketball/international/sea-games/14516',
                        'https://www.sofascore.com/tournament/basketball/spain/copa-del-rey/396',
                        'https://www.sofascore.com/tournament/basketball/kosovo/superkupa-e-kosoves/17213',
                        'https://www.sofascore.com/tournament/basketball/international/fiba-asia-cup-women/14237',
                        'https://www.sofascore.com/tournament/basketball/austria/zweite-liga/20082',
                        'https://www.sofascore.com/tournament/basketball/argentina/super-20/10701',
                        'https://www.sofascore.com/tournament/basketball/international/u18-fiba-eurobasket-div-b/896',
                        'https://www.sofascore.com/tournament/basketball/international/fiba-centrobasket-championship-women/1814',
                        'https://www.sofascore.com/tournament/basketball/sweden/superettan/20174',
                        'https://www.sofascore.com/tournament/basketball/england/bbl-trophy/2360',
                        'https://www.sofascore.com/tournament/basketball/israel/wbl-women/20078',
                        'https://www.sofascore.com/tournament/basketball/croatia-amateur/kozjak-basket-3x3/20592',
                        'https://www.sofascore.com/tournament/basketball/usa/nba-rising-stars-challenge/11015',
                        'https://www.sofascore.com/tournament/basketball/international/u20-european-challengers/17050',
                        'https://www.sofascore.com/tournament/basketball/international/u19-world-cup-women/897',
                        'https://www.sofascore.com/tournament/basketball/philippines/pba-governors-cup/1712',
                        'https://www.sofascore.com/tournament/basketball/international/u18-fiba-asia-cup/9343',
                        'https://www.sofascore.com/tournament/basketball/france/leaders-cup-lnb/405',
                        'https://www.sofascore.com/tournament/basketball/greece/b-ethniki/19769',
                        'https://www.sofascore.com/tournament/basketball/international/fiba-eurobasket/285',
                        'https://www.sofascore.com/tournament/basketball/slovenia/super-cup/2330',
                        'https://www.sofascore.com/tournament/basketball/international/central-american-and-caribbean-games-women/11300',
                        'https://www.sofascore.com/tournament/basketball/international/olympic-games-women-qual/663',
                        'https://www.sofascore.com/tournament/basketball/australia/nbl1-women-east/18404',
                        'https://www.sofascore.com/tournament/basketball/international/champions-league-americas/14360',
                        'https://www.sofascore.com/tournament/basketball/greece-amateur/a2-eskak/20794',
                        'https://www.sofascore.com/tournament/basketball/croatia-amateur/crohoops-division-i/16654',
                        'https://www.sofascore.com/tournament/basketball/international/u20-fiba-eurobasket-div-b/894',
                        'https://www.sofascore.com/tournament/basketball/portugal/taca-hugo-dos-santos/18513',
                        'https://www.sofascore.com/tournament/basketball/brazil/copa-super-8/19892',
                        'https://www.sofascore.com/tournament/basketball/international/asean-basketball-league/1756',
                        'https://www.sofascore.com/tournament/basketball/international/fiba-afrobasket/931',
                        'https://www.sofascore.com/tournament/basketball/usa/overtime-elite/19932',
                        'https://www.sofascore.com/tournament/basketball/international/fiba-eurobasket-qual/662',
                        'https://www.sofascore.com/tournament/basketball/international/commonwealth-games-women/11041',
                        'https://www.sofascore.com/tournament/basketball/international/fiba-eurobasket-women-qual/1070',
                        'https://www.sofascore.com/tournament/basketball/international/fiba-world-cup/441',
                        'https://www.sofascore.com/tournament/basketball/international/u20-fiba-eurobasket-div-a/893',
                        'https://www.sofascore.com/tournament/basketball/austria/super-cup/1498',
                        'https://www.sofascore.com/tournament/basketball/international/fiba-womens-americup/730',
                        'https://www.sofascore.com/tournament/basketball/croatia-amateur/koala/19595',
                        'https://www.sofascore.com/tournament/basketball/international/commonwealth-games/11040',
                        'https://www.sofascore.com/tournament/basketball/poland/superpuchar/1183',
                        'https://www.sofascore.com/tournament/basketball/turkey/turkiye-kupasi/1179',
                        'https://www.sofascore.com/tournament/basketball/australia/nbl1/13487',
                        'https://www.sofascore.com/tournament/basketball/usa/college-basketball-invitational/18638',
                        'https://www.sofascore.com/tournament/basketball/germany/all-star-game/2046',
                        'https://www.sofascore.com/tournament/basketball/australia/nbl1-wildcard/18601',
                        'https://www.sofascore.com/tournament/basketball/romania/cup/19939',
                        'https://www.sofascore.com/tournament/basketball/international/asian-games-women/11343',
                        'https://www.sofascore.com/tournament/basketball/greece/super-cup/17267',
                        'https://www.sofascore.com/tournament/basketball/greece-amateur/a-eskavde/19930',
                        'https://www.sofascore.com/tournament/basketball/international/u19-world-cup/887',
                        'https://www.sofascore.com/tournament/basketball/international/olympic-games-qualification/432',
                        'https://www.sofascore.com/tournament/basketball/international/u20-fiba-eurobasket-div-a-women/888',
                        'https://www.sofascore.com/tournament/basketball/international/fiba-asia-cup/943',
                        'https://www.sofascore.com/tournament/basketball/international/fiba-world-cup-qualification-africa/10460',
                        'https://www.sofascore.com/tournament/basketball/international/club-friendly-games/1195',
                        'https://www.sofascore.com/tournament/basketball/international/basketball-africa-league/16968',
                        'https://www.sofascore.com/tournament/basketball/australia/nbl-1-wildcard-women/18552',
                        'https://www.sofascore.com/tournament/basketball/greece-amateur/a1-eskak/19727',
                        'https://www.sofascore.com/tournament/basketball/china/cba-rookie-game/16767',
                        'https://www.sofascore.com/tournament/basketball/international/fiba-world-cup-qualification-europe/10437',
                        'https://www.sofascore.com/tournament/basketball/turkey/super-cup/1500',
                        'https://www.sofascore.com/tournament/basketball/romania/romanian-basketball-cup-women/19938',
                        'https://www.sofascore.com/tournament/basketball/usa/the-basketball-classic/18591',
                        'https://www.sofascore.com/tournament/basketball/international/torneo-interligas/14093',
                        'https://www.sofascore.com/tournament/basketball/hungary/magyar-kupa/20057',
                        'https://www.sofascore.com/tournament/basketball/international/baltic-basketball-league/582',
                        'https://www.sofascore.com/tournament/basketball/international/fiba-afrocan/13827',
                        'https://www.sofascore.com/tournament/basketball/international/pan-american-games-women/13868',
                        'https://www.sofascore.com/tournament/basketball/greece-amateur/a-eskana/19839',
                        'https://www.sofascore.com/tournament/basketball/china/cba-all-star-game/2051',
                        'https://www.sofascore.com/tournament/basketball/international/nba-africa-game/11270',
                        'https://www.sofascore.com/tournament/basketball/usa/ncaa-division-iii-national-championship/14735',
                        'https://www.sofascore.com/tournament/basketball/italy/final-eight/877',
                        'https://www.sofascore.com/tournament/basketball/slovakia/cup/1636',
                        'https://www.sofascore.com/tournament/basketball/italy/supercoppa-lnp/9466',
                        'https://www.sofascore.com/tournament/basketball/usa/wnba-commissioner-s-cup/18949',
                        'https://www.sofascore.com/tournament/basketball/international/fiba-world-cup-qualification-asia-oceania/10486',
                        'https://www.sofascore.com/tournament/basketball/usa/wnba-all-star-game/1329',
                        'https://www.sofascore.com/tournament/basketball/france/match-des-champions/1155',
                        'https://www.sofascore.com/tournament/basketball/greece-amateur/a1-halkidikis/19800',
                        'https://www.sofascore.com/tournament/basketball/international/fiba-americup/681',
                        'https://www.sofascore.com/tournament/basketball/spain/supercopa-femenina/14200',
                        'https://www.sofascore.com/tournament/basketball/france/nationale-1/18249',
                        'https://www.sofascore.com/tournament/basketball/poland/polish-basketball-cup/14700',
                        'https://www.sofascore.com/tournament/basketball/international/u20-european-challengers-women/17048',
                        'https://www.sofascore.com/tournament/basketball/bulgaria/cup/20083',
                        'https://www.sofascore.com/tournament/basketball/international/fiba-centrobasket-championship/1798',
                        'https://www.sofascore.com/tournament/basketball/brazil/paraense/20691',
                        'https://www.sofascore.com/tournament/basketball/international/fiba-afrobasket-women/2143',
                        'https://www.sofascore.com/tournament/basketball/italy/supercoppa/1157',
                        'https://www.sofascore.com/tournament/basketball/international/fiba-south-american-championship-women/1816',
                        'https://www.sofascore.com/tournament/basketball/philippines/pba-on-tour/20589',
                        'https://www.sofascore.com/tournament/basketball/portugal/campeonato-nacional-liga-feminina/20157',
                        'https://www.sofascore.com/tournament/basketball/serbia/radivoj-korac-cup/10188',
                        'https://www.sofascore.com/tournament/basketball/bosnia-herzegovina/druga-liga-republike-srpske-centar/20334',
                        'https://www.sofascore.com/tournament/basketball/usa/nba-all-star-game/875',
                        'https://www.sofascore.com/tournament/basketball/usa/ncaa-division-ii-national-championship/13424',
                        'https://www.sofascore.com/tournament/basketball/usa/the-basketball-tournament/19020',
                        'https://www.sofascore.com/tournament/basketball/finland/1-division/20114',
                        'https://www.sofascore.com/tournament/basketball/israel/league-cup/1193',
                        'https://www.sofascore.com/tournament/basketball/international/fiba-south-american-championship/1796',

                        # Estás ligas las voy a hacer individualmente por problemas especificos de XPATH
                        'https://www.sofascore.com/tournament/basketball/international/eurocup/141#42900',
                        'https://www.sofascore.com/tournament/basketball/usa/ncaa-men/648',
                        'https://www.sofascore.com/tournament/basketball/usa/ncaa-march-madness-division-1/13434',
                        'https://www.sofascore.com/tournament/basketball/usa/ncaa-division-i-national-championship-women/16718',
                        'https://www.sofascore.com/tournament/basketball/usa/ncaa-women/10664',
                        'https://www.sofascore.com/tournament/basketball/international/balkan-international-basketball-league/2003',
                        'https://www.sofascore.com/tournament/basketball/international/eurocup/141',

                        # Estás ligas ya tienen su .csv listo
                        'https://www.sofascore.com/tournament/basketball/argentina/lnb/1680',
                        'https://www.sofascore.com/tournament/basketball/usa/nba/132'
                    ]

    return list_del_link

