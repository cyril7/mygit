//在表格的第一列中查找等于指定ID的行
function SearchIdInTable(tablerow, findid)
{
    var i;
    var tablerownum = tablerow.length;
	for (i = 1; i < tablerownum; i++)
		if ($("#Table tr:eq(" + i + ") td:eq(0)").html() == findid)
			return i;
	return -1;
}
//用CSS控制奇偶行的颜色
function SetTableRowColor()
{
	$("#Table tr:odd").css("background-color", "#e6e6fa");
$("#Table tr:even").css("background-color", "#fff0fa");
$("#Table tr:odd").hover(
	function(){$(this).css("background-color", "orange");},
	function(){$(this).css("background-color", "#e6e6fa");}		
);
$("#Table tr:even").hover(
	function(){$(this).css("background-color", "orange");},
	function(){$(this).css("background-color", "#fff0fa");}		
);
}
//响应edit按钮
function editFun(id, name, age)
{
    $("#editdiv").show();
    $("#adddiv").hide();

    $("#editdiv_id").val(id);
    $("#editdiv_name").val(name);
    $("#editdiv_age").val(age);
}
//响应add按钮
function addFun()
{
    $("#editdiv").hide();
    $("#adddiv").show();    
}
//记录条数增加
function IncTableRowCount()
{
	var tc = $("#tableRowCount");
	tc.html(parseInt(tc.html()) + 1);
}
//记录条数减少
function DecTableRowCount()
{
	var tc = $("#tableRowCount");
	tc.html(parseInt(tc.html()) - 1);
}
//增加一行
function addRowInTable(id, name, age)
{
    //新增加一行
    var appendstr = "<tr>";
    appendstr += "<td>" + id + "</td>";
    appendstr += "<td>" + name + "</td>";
    appendstr += "<td>" + age + "</td>";
    appendstr += "<td><input type=\"button\" value=\"Edit\" onclick=\"editFun(id, name, age);\" />\t";
    appendstr += "<input type=\"button\" value=\"Delete\" onclick=\"deleteFun(id)\" /></td>";
    appendstr += "</tr>";       	
    $("#Table").append(appendstr);
    IncTableRowCount();
}
//修改某一行
function updataRowInTable(id, newname, newage)
{
    var i = SearchIdInTable($("#Table tr"), id);
    if (i != -1)
    {
	    $("#Table tr:eq(" + i + ") td:eq(1)").html(newname != "" ? newname : " ");
        $("#Table tr:eq(" + i + ") td:eq(2)").html(newage != "" ? newage : " ");
        $("#editdiv").hide();
    }
}
//删除某一行
function deleteRowInTable(id)
{
	var i = SearchIdInTable($("#Table tr"), id);
	if (i != -1)
	{	
		//删除表格中该行
		$("#Table tr:eq(" + i + ")").remove();
		SetTableRowColor();
		DecTableRowCount();
	}
}
//增加删除修改数据库函数 通过AJAX与服务器通信
function insertFun()
{
    var name = $("#adddiv_name").val();
    var age = $("#adddiv_age").val();

    if (name == "" || age == "")
    {
	    alert("请输入名字和年龄!");
	    return ;
    }

    //submit to server 返回插入数据的id
    $.post("insert.php", {name:name, age:age}, function(data){
        if (data == "f")
        {
            alert("Insert date failed");
        }
        else
        {
        	addRowInTable(data, name, age);
    	    SetTableRowColor();
    	    $("#adddiv").hide();
        }
    });
}
function deleteFun(id)
{
	if (confirm("确认删除?"))
	{
		//submit to server
		$.post("delete.php", {id:id}, function(data){
			if (data == "f")
			{
			  alert("delete date failed");
			}
			else
			{
                deleteRowInTable(id);
			}
	    });
	}
}
function updataFun()
{
    var id = $("#editdiv_id").val();
    var name = $("#editdiv_name").val();
    var age = $("#editdiv_age").val(); 

    //submit to server
    $.post("updata.php", {id:id, name:name, age:age}, function(data){
        if (data == "f")
        {
            alert("Updata date failed");
        }
        else
        {
            updataRowInTable(id, name, age);
	    }
    });
}
  
$(document).ready(function()
{
	SetTableRowColor();
	//UpdataTableRowCount();
}); 
