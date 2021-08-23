
j_diameter=88846.0
j_d_to_sun=483632000.0
e_diamter=7926
e_d_to_sun=92957100.0
speed_light_s=186000

r_j_e_of_sun=j_d_to_sun/e_d_to_sun
print "the ratio of Jupiter’s distance from the Sun to that of the Earth is,",r_j_e_of_sun
v_j_e_of_sun=j_diameter/e_diamter
print "the ratio of Jupiter’s volume to that of the Earth,",v_j_e_of_sun
t_light_s_e=int(e_d_to_sun/speed_light_s)
min_t_light_s_e=t_light_s_e/60
sec_t_light_s_e=t_light_s_e%60
print "the time is",min_t_light_s_e," mins and",sec_t_light_s_e,"seconds it takes light to travel from the Sun to Earth"
