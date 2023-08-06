## coding: utf-8
##<%inherit file="/layout_clean.mako" />
<%inherit file="/layout.mako"/>

## set this to False to avoid POST issues in saveComment
<%page cached="False" />

<%namespace file="components.mako" import="headline" />

<%namespace file="blogentry_comment_thread.mako" import="comments_for_item" />


<%def name="pagetitle(text='foo')" cached="False">
<% result = data['result'] %>
${result}
</%def>

##<%def name="pagemeta()">
##<%
##result = data['result']
##tagstr = ''.join(["%s," % item.name for item in result.m.tags()])
##tagstr = tagstr.rstrip(',')
##%>
## <link rel="alternate" type="text/rss" ...>
## <meta name="author" content="${result.author}" />
## <meta name="description" content="${result.short_description}" />
##<meta name="keywords" content="${tagstr}" />
##</%def>

<%def name="pagecontent()">
<% 
result = data['result'] 
##addthis_widget = data.get('addthis_widget', 'addthis widget is disabled')
comment_form = data['comment_form']
media_prefix = data['MEDIA_URL']
comments = data['comments']
comment_count = len(comments)
%>
<div class="fl" style="width:290px">
<div class="ui-generic ui-rounded b1 whitebg">
${headline(result, fulltext=True)}
</div>
<div class="ui-generic ui-rounded b1 whitebg">
${comments_for_item()}
</div>

<br class="clear"/>
</div>

<br class="clear"/>

## script for comments (ajax)
##<script type="text/javascript" src="${media_prefix}js/tm_api-2.0/src/formvalidator.js">
##</script>
##<script>
##(function(j){
##  j('#commentBtn').bind('click', function(){
##   j('#commentform').saveForm({
##        href: "comment/new/",
##        callback: function(data, msg){
##            //buggy or insane jquery ui dialog
##            //j(this).SimpleDialog('Your comment has been saved!', 'Thank you');
##        },     
##    }); 
##   });
##})(jQuery);
##</script>

</%def>
${self.pagecontent()}
