using System;
using System.Collections.Generic;
using Microsoft.AspNetCore.SignalR;

//From
//https://radu-matei.github.io/blog/signalr-core/

public class ChatHub : Hub
{
    public static List<string> ConnectedUsers;

    public void Send(string originatorUser, string message)
    {
        Clients.All.messageReceived(originatorUser, message);
    }

    public void Connect(string newUser)
    {
        if (ConnectedUsers == null)
            ConnectedUsers = new List<string>();

        ConnectedUsers.Add(newUser);
        Clients.Caller.getConnectedUsers(ConnectedUsers);
        Clients.Others.newUserAdded(newUser);
    }
}
