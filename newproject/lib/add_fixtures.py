
#!/usr/bin/env python

# Add relative paths to python path, so we can see insrep and django modules
import sys, os
sys.path.append('..')
sys.path.append('../..')

# Fire up Django
from django.core.management import setup_environ

### CHANGE THIS ## from projectname import settings

setup_environ(settings)

# Get the classes and modules we need
from common.models import SEOMetatag, Page, ReferenceContent

#timestamp for capturing data
import datetime
import os

SEOMetatag.objects.filter().delete()
Page.objects.filter().delete()
ReferenceContent.objects.filter().delete()
HomeImage.objects.filter().delete()

#adding the fixtures
SEOMetatag(
    display_type = 'global',
    meta_title = '',
    meta_description = '',
    meta_keywords = '',
).save()



page = Page(
    title="About Us",
    slug="about-us",
    display=True,
    content="""
	About Us Coming Soon!<br/><br/>
	<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam malesuada gravida purus, 
	feugiat facilisis augue vulputate id. In laoreet, metus nec fermentum ultrices, lorem orci 
	pharetra turpis, nec auctor nisi quam ac purus. In mollis semper blandit. Suspendisse vitae 
	arcu tellus. Pellentesque tincidunt nibh non augue adipiscing in posuere purus facilisis. 
	Maecenas vehicula nunc nulla, eget facilisis elit. Etiam et justo eget enim imperdiet euismod. 
	Donec sagittis libero nibh. Nulla dolor lorem, rutrum vel scelerisque eget, vestibulum mollis 
	quam. Nullam ut urna ut risus elementum mattis non eu urna. Nulla facilisi. <br/>
	<br/>
	Nam at sem eu magna porta ornare et sit amet enim. Vestibulum ante ipsum primis in faucibus 
	orci luctus et ultrices posuere cubilia Curae; Pellentesque dignissim arcu sit amet tellus 
	rutrum eu venenatis tortor interdum. <br />
	<br />
	Donec id enim et nulla cursus consectetur posuere eget ante. Vivamus magna dui, lobortis ac 
	elementum sed, porttitor quis elit. Aliquam lobortis lectus posuere elit aliquet at rhoncus 
	diam placerat. Maecenas eu massa a urna tristique blandit a ac magna. Pellentesque lacinia 
	dolor sed tortor rutrum hendrerit in eget lorem. Aliquam erat volutpat. Proin vehicula nibh 
	vitae libero commodo convallis fringilla odio hendrerit. Suspendisse potenti. Aliquam lacinia 
	tellus est. Nunc et lectus ut diam sollicitudin euismod a sed dui. Nullam ornare urna quis 
	massa accumsan auctor. <br />
	<br />
	Nulla auctor ligula vel augue pellentesque ac volutpat dui accumsan. Curabitur lacinia tortor 
	quis est congue ornare. Curabitur varius egestas turpis, at tempus odio lobortis in. Morbi 
	nibh nisi, fermentum non rutrum vel, faucibus sed dolor. Nam sit amet risus at sapien feugiat 
	aliquet. Ut vitae ipsum et mauris condimentum adipiscing. Donec sodales, neque ut pulvinar 
	vestibulum, nisl purus gravida dolor, nec pellentesque magna purus non lectus. Vestibulum et 
	risus quis arcu mattis mollis. Etiam blandit erat a odio aliquet sit amet volutpat ligula mattis. 
	Etiam tempus, ipsum sagittis commodo lobortis, odio justo viverra purus, porta posuere velit mi 
	a justo. Sed ornare sollicitudin purus, ut vehicula justo tristique non. Aliquam malesuada 
	congue felis non auctor. Aenean vitae lorem eu odio lacinia dignissim. Aliquam vitae eros quis 
	metus congue interdum eget sit amet libero. Nulla facilisi. Duis eu est eget elit rutrum auctor.</p>
	""",
).save()



page = Page(
    title="FAQ",
    slug="faq",
    display=True,
    content="""
	Frequently Asked Questions Coming Soon!<br/><br/>
	<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam malesuada gravida purus, 
	feugiat facilisis augue vulputate id. In laoreet, metus nec fermentum ultrices, lorem orci 
	pharetra turpis, nec auctor nisi quam ac purus. In mollis semper blandit. Suspendisse vitae 
	arcu tellus. Pellentesque tincidunt nibh non augue adipiscing in posuere purus facilisis. 
	Maecenas vehicula nunc nulla, eget facilisis elit. Etiam et justo eget enim imperdiet euismod. 
	Donec sagittis libero nibh. Nulla dolor lorem, rutrum vel scelerisque eget, vestibulum mollis 
	quam. Nullam ut urna ut risus elementum mattis non eu urna. Nulla facilisi. <br/>
	<br/>
	Nam at sem eu magna porta ornare et sit amet enim. Vestibulum ante ipsum primis in faucibus 
	orci luctus et ultrices posuere cubilia Curae; Pellentesque dignissim arcu sit amet tellus 
	rutrum eu venenatis tortor interdum. <br />
	<br />
	Donec id enim et nulla cursus consectetur posuere eget ante. Vivamus magna dui, lobortis ac 
	elementum sed, porttitor quis elit. Aliquam lobortis lectus posuere elit aliquet at rhoncus 
	diam placerat. Maecenas eu massa a urna tristique blandit a ac magna. Pellentesque lacinia 
	dolor sed tortor rutrum hendrerit in eget lorem. Aliquam erat volutpat. Proin vehicula nibh 
	vitae libero commodo convallis fringilla odio hendrerit. Suspendisse potenti. Aliquam lacinia 
	tellus est. Nunc et lectus ut diam sollicitudin euismod a sed dui. Nullam ornare urna quis 
	massa accumsan auctor. <br />
	<br />
	Nulla auctor ligula vel augue pellentesque ac volutpat dui accumsan. Curabitur lacinia tortor 
	quis est congue ornare. Curabitur varius egestas turpis, at tempus odio lobortis in. Morbi 
	nibh nisi, fermentum non rutrum vel, faucibus sed dolor. Nam sit amet risus at sapien feugiat 
	aliquet. Ut vitae ipsum et mauris condimentum adipiscing. Donec sodales, neque ut pulvinar 
	vestibulum, nisl purus gravida dolor, nec pellentesque magna purus non lectus. Vestibulum et 
	risus quis arcu mattis mollis. Etiam blandit erat a odio aliquet sit amet volutpat ligula mattis. 
	Etiam tempus, ipsum sagittis commodo lobortis, odio justo viverra purus, porta posuere velit mi 
	a justo. Sed ornare sollicitudin purus, ut vehicula justo tristique non. Aliquam malesuada 
	congue felis non auctor. Aenean vitae lorem eu odio lacinia dignissim. Aliquam vitae eros quis 
	metus congue interdum eget sit amet libero. Nulla facilisi. Duis eu est eget elit rutrum auctor.</p>
	""",
).save()


page = Page(
    title="Terms &amp; Conditions",
    slug="terms-and-conditions",
    display=True,
    content="""
	Terms &amp; Conditions Coming Soon!<br/><br/>
	<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam malesuada gravida purus, 
	feugiat facilisis augue vulputate id. In laoreet, metus nec fermentum ultrices, lorem orci 
	pharetra turpis, nec auctor nisi quam ac purus. In mollis semper blandit. Suspendisse vitae 
	arcu tellus. Pellentesque tincidunt nibh non augue adipiscing in posuere purus facilisis. 
	Maecenas vehicula nunc nulla, eget facilisis elit. Etiam et justo eget enim imperdiet euismod. 
	Donec sagittis libero nibh. Nulla dolor lorem, rutrum vel scelerisque eget, vestibulum mollis 
	quam. Nullam ut urna ut risus elementum mattis non eu urna. Nulla facilisi. <br/>
	<br/>
	Nam at sem eu magna porta ornare et sit amet enim. Vestibulum ante ipsum primis in faucibus 
	orci luctus et ultrices posuere cubilia Curae; Pellentesque dignissim arcu sit amet tellus 
	rutrum eu venenatis tortor interdum. <br />
	<br />
	Donec id enim et nulla cursus consectetur posuere eget ante. Vivamus magna dui, lobortis ac 
	elementum sed, porttitor quis elit. Aliquam lobortis lectus posuere elit aliquet at rhoncus 
	diam placerat. Maecenas eu massa a urna tristique blandit a ac magna. Pellentesque lacinia 
	dolor sed tortor rutrum hendrerit in eget lorem. Aliquam erat volutpat. Proin vehicula nibh 
	vitae libero commodo convallis fringilla odio hendrerit. Suspendisse potenti. Aliquam lacinia 
	tellus est. Nunc et lectus ut diam sollicitudin euismod a sed dui. Nullam ornare urna quis 
	massa accumsan auctor. <br />
	<br />
	Nulla auctor ligula vel augue pellentesque ac volutpat dui accumsan. Curabitur lacinia tortor 
	quis est congue ornare. Curabitur varius egestas turpis, at tempus odio lobortis in. Morbi 
	nibh nisi, fermentum non rutrum vel, faucibus sed dolor. Nam sit amet risus at sapien feugiat 
	aliquet. Ut vitae ipsum et mauris condimentum adipiscing. Donec sodales, neque ut pulvinar 
	vestibulum, nisl purus gravida dolor, nec pellentesque magna purus non lectus. Vestibulum et 
	risus quis arcu mattis mollis. Etiam blandit erat a odio aliquet sit amet volutpat ligula mattis. 
	Etiam tempus, ipsum sagittis commodo lobortis, odio justo viverra purus, porta posuere velit mi 
	a justo. Sed ornare sollicitudin purus, ut vehicula justo tristique non. Aliquam malesuada 
	congue felis non auctor. Aenean vitae lorem eu odio lacinia dignissim. Aliquam vitae eros quis 
	metus congue interdum eget sit amet libero. Nulla facilisi. Duis eu est eget elit rutrum auctor.</p>
""",
).save()

page = Page(
    title="Privacy Policy",
    slug="privacy-policy",
    display=True,
    content="""
	Privacy Policy Coming Soon!<br/><br/>
	<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam malesuada gravida purus, 
	feugiat facilisis augue vulputate id. In laoreet, metus nec fermentum ultrices, lorem orci 
	pharetra turpis, nec auctor nisi quam ac purus. In mollis semper blandit. Suspendisse vitae 
	arcu tellus. Pellentesque tincidunt nibh non augue adipiscing in posuere purus facilisis. 
	Maecenas vehicula nunc nulla, eget facilisis elit. Etiam et justo eget enim imperdiet euismod. 
	Donec sagittis libero nibh. Nulla dolor lorem, rutrum vel scelerisque eget, vestibulum mollis 
	quam. Nullam ut urna ut risus elementum mattis non eu urna. Nulla facilisi. <br/>
	<br/>
	Nam at sem eu magna porta ornare et sit amet enim. Vestibulum ante ipsum primis in faucibus 
	orci luctus et ultrices posuere cubilia Curae; Pellentesque dignissim arcu sit amet tellus 
	rutrum eu venenatis tortor interdum. <br />
	<br />
	Donec id enim et nulla cursus consectetur posuere eget ante. Vivamus magna dui, lobortis ac 
	elementum sed, porttitor quis elit. Aliquam lobortis lectus posuere elit aliquet at rhoncus 
	diam placerat. Maecenas eu massa a urna tristique blandit a ac magna. Pellentesque lacinia 
	dolor sed tortor rutrum hendrerit in eget lorem. Aliquam erat volutpat. Proin vehicula nibh 
	vitae libero commodo convallis fringilla odio hendrerit. Suspendisse potenti. Aliquam lacinia 
	tellus est. Nunc et lectus ut diam sollicitudin euismod a sed dui. Nullam ornare urna quis 
	massa accumsan auctor. <br />
	<br />
	Nulla auctor ligula vel augue pellentesque ac volutpat dui accumsan. Curabitur lacinia tortor 
	quis est congue ornare. Curabitur varius egestas turpis, at tempus odio lobortis in. Morbi 
	nibh nisi, fermentum non rutrum vel, faucibus sed dolor. Nam sit amet risus at sapien feugiat 
	aliquet. Ut vitae ipsum et mauris condimentum adipiscing. Donec sodales, neque ut pulvinar 
	vestibulum, nisl purus gravida dolor, nec pellentesque magna purus non lectus. Vestibulum et 
	risus quis arcu mattis mollis. Etiam blandit erat a odio aliquet sit amet volutpat ligula mattis. 
	Etiam tempus, ipsum sagittis commodo lobortis, odio justo viverra purus, porta posuere velit mi 
	a justo. Sed ornare sollicitudin purus, ut vehicula justo tristique non. Aliquam malesuada 
	congue felis non auctor. Aenean vitae lorem eu odio lacinia dignissim. Aliquam vitae eros quis 
	metus congue interdum eget sit amet libero. Nulla facilisi. Duis eu est eget elit rutrum auctor.</p>
""",
).save()


reference_content = ReferenceContent(
    title="Contact Information",
    reference="contact",
    display=True,
    content="""
	We welcome any questions you may have about ProjectName. Please enter your questions into the contact-box and we will respond as soon as possible. We look forward to communicating with you!<br>
	<br>
	You may alternatively speak to a member of the ProjectName team by phoning one of the numbers below:<br>
	<br>
	<table cellpadding="5" cellpadding="5" class="tableContactPeople">
	    <tr>
	        <td width="140px"><strong>ContactName: </strong></td><td>+27 70 000 0000</td>
	    </tr>
	</table>
	<br>
	<u>Our physical address is:</u><br>
	<br>
	<strong>Company Name</strong><br>
	StreetAddress<br>
	Business Park<br>
	Road, Suburb C0D3<br>
	Cape Town, South Africa<br>
	<br>
	Thank you.<br>
	<br>
	The Company Team.<br>
""",
).save()