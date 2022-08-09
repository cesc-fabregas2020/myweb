program main
implicit none
integer::n,istat
character(len=180)::pline
open(11,file='out.dat')
n=0
do
  read(11,'(a180)',iostat=istat) pline
  if(istat.ne.0) exit
  if(pline(1:2).eq."['") then
    n=n+1
    write(5005,'(a180)') pline
  endif
enddo
close(11)
write(*,*) n
end
